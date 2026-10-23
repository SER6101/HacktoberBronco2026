import { useCallback, useEffect, useRef, useState } from "react";
import { hobbies, skillDescriptions } from "../data/hobbies.js";
import { getHobbyInfo, selectSkill, getProgress, getLesson, completeLesson, getAchievements } from "../services/api.js";

export default function HobbyProgressPage({ user, hobbyName, sessionId, onBack, onSaveSkill, onProgressSaved }) {
  const meta = hobbies.find((h) => h.name === hobbyName);
  const savedSkill = user.skillLevels?.[hobbyName] || "";
  const [skill, setSkill] = useState(savedSkill);
  const [selectedSkill, setSelectedSkill] = useState("");
  const [showPopup, setShowPopup] = useState(!savedSkill);
  const [info, setInfo] = useState(null);
  const [progress, setProgress] = useState(null);
  const [lessonData, setLessonData] = useState(null);
  const [current, setCurrent] = useState(null);
  const [achievements, setAchievements] = useState({});
  const [quests, setQuests] = useState([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [readingPercent, setReadingPercent] = useState(0);
  const [videoPercent, setVideoPercent] = useState(0);
  const submitting = useRef(false);
  const lastReported = useRef(null);
  const progressSavedRef = useRef(onProgressSaved);
  progressSavedRef.current = onProgressSaved;

  useEffect(() => {
    getHobbyInfo(hobbyName).then(setInfo).catch((e) => setError(e.message));
  }, [hobbyName]);

  const refresh = useCallback(async (level, desiredLesson = null) => {
    const [result, pageData] = await Promise.all([
      getProgress(hobbyName, level, sessionId),
      selectSkill(hobbyName, level, sessionId),
    ]);
    setQuests(pageData.page?.sidebar?.quests || []);
    setProgress(result);
    const number = desiredLesson ?? result.progress.current_lesson;
    const detail = await getLesson(hobbyName, number, level, sessionId);
    setCurrent(number);
    setLessonData(detail);
    const badges = await getAchievements(hobbyName, sessionId, level);
    setAchievements(badges.achievements || {});
    // SQLite stores real completions; auto-credited nodes are included for display.
    progressSavedRef.current?.(hobbyName, result.completed_lessons);
  }, [hobbyName, sessionId]);

  useEffect(() => {
    if (!skill) return;
    setError("");
    refresh(skill).catch((e) => setError(e.message));
  }, [skill, refresh]);

  async function chooseSkill() {
    if (!selectedSkill || busy) return;
    setBusy(true); setError("");
    try {
      await selectSkill(hobbyName, selectedSkill, sessionId);
      if (!onSaveSkill(hobbyName, selectedSkill)) throw new Error("Could not save skill selection");
      setSkill(selectedSkill);
      setShowPopup(false);
    } catch (e) { setError(e.message); }
    finally { setBusy(false); }
  }

  async function openLesson(number) {
    if (!skill) return;
    setBusy(true); setError("");
    try {
      const detail = await getLesson(hobbyName, number, skill, sessionId);
      setCurrent(number); setLessonData(detail);
      setReadingPercent(0); setVideoPercent(0);
      lastReported.current = null;
    } catch (e) { setError(e.message); }
    finally { setBusy(false); }
  }

  async function reportCompletion(kind) {
    if (!skill || current === null || submitting.current || lessonData?.status?.completed) return;
    if (lastReported.current === `${skill}:${current}`) return;
    submitting.current = true;
    setError("");
    try {
      await completeLesson(hobbyName, sessionId, skill, current, kind === "reading", kind === "video");
      lastReported.current = `${skill}:${current}`;
      await refresh(skill, current);
    } catch (e) { setError(e.message); }
    finally { submitting.current = false; }
  }

  function handleReadingScroll(event) {
    if (lessonData?.status?.completed) return;
    const el = event.currentTarget;
    const max = el.scrollHeight - el.clientHeight;
    const pct = max <= 0 ? 100 : Math.min(100, Math.round(el.scrollTop / max * 100));
    setReadingPercent(pct);
    if (el.scrollTop + el.clientHeight >= el.scrollHeight - 4) reportCompletion("reading");
  }

  const lesson = lessonData?.lesson;
  const status = lessonData?.status;
  const roadmap = progress?.roadmap || [];
  const completedCount = progress?.progress?.completed || 0;
  const percent = progress?.progress?.percentage || 0;
  const completedQuests = []; // Quest storage is not yet implemented in SQLite.
  const questTitles = quests;

  return (
    <main className="wide">
      <button className="text-button back" onClick={onBack}>← My hobbies</button>
      <section className="progress-heading">
        <span className="big-icon">{meta?.icon || "✦"}</span>
        <div className="hobby-heading"><p className="eyebrow">YOUR HOBBY JOURNEY</p><h1>{hobbyName}</h1><p>{info?.description || meta?.description}</p></div>
      </section>
      {error && <p className="error" role="alert">{error}</p>}
      {skill && progress && <>
        <section className="panel" style={{ marginBottom: 20 }}>
          <div className="panel-heading"><div><p className="eyebrow">YOUR LEARNING PATH</p><h2>10-lesson roadmap</h2></div><small>{completedCount}/10 complete</small></div>
          <div className="roadmap" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(120px, 1fr))", gap: 10 }}>
            {roadmap.map((node) => <button key={node.node} type="button"
              className={`roadmap-step${node.node === current ? " active" : ""}${node.completed ? " done" : ""}`}
              disabled={!node.unlocked || busy} onClick={() => openLesson(node.node)}
              aria-label={`Lesson ${node.node}: ${node.title}${node.completed ? ", completed" : node.unlocked ? ", available" : ", locked"}`}>
              <span className="marker">{node.completed ? "✓" : String(node.node).padStart(2, "0")}</span>
              <span className="roadmap-copy"><strong>{node.title}</strong><small>{node.auto_completed ? "Credited by skill" : node.completed ? "Completed" : node.unlocked ? "Available" : "Locked"}</small></span>
            </button>)}
          </div>
        </section>
        <div className="learning-layout">
          <section className="panel">
            {lesson && <>
              <p className="eyebrow">LESSON {current} OF 10</p>
              <h2>{lesson.title}</h2>
              {lesson.reading && <>
                <p className="muted">Scroll to the end of the article to complete this lesson.</p>
                <div key={`${skill}:${current}:reading`} onScroll={handleReadingScroll}
                  style={{ maxHeight: 280, overflowY: "auto", border: "1px solid #ddd", borderRadius: 12, padding: 20, lineHeight: 1.7 }}>
                  <article style={{ whiteSpace: "pre-wrap" }}>{lesson.reading}</article>
                  <p className="muted">End of lesson reading.</p>
                </div>
                <p className="muted">Reading progress: {status?.completed ? 100 : readingPercent}%</p>
                <progress value={status?.completed ? 100 : readingPercent} max="100" style={{ width: "100%" }} />
                {/* Short content might not scroll. Explicit end-of-article visibility handles that case. */}
                {!status?.completed && <ReadingEndObserver key={`${skill}:${current}:end`} onReached={() => reportCompletion("reading")} />}
              </>}
              {lesson.video_url && <div className="tutorial">
                <p className="eyebrow">VIDEO LESSON</p>
                <video key={`${skill}:${current}:video`} controls width="100%"
                  onTimeUpdate={(e) => { const v = e.currentTarget; if (Number.isFinite(v.duration) && v.duration > 0) setVideoPercent(Math.round(v.currentTime / v.duration * 100)); }}
                  onEnded={() => reportCompletion("video")} src={lesson.video_url} />
                <p className="muted">Video progress: {status?.completed ? 100 : videoPercent}%</p>
              </div>}
              {status?.completed ? <p className="complete-msg">✓ Lesson completed — next lesson unlocked.</p> : <p className="muted">Finish the reading or video to unlock Next Lesson.</p>}
              <div className="actions">
                <button className="button light" disabled={current <= 1 || busy} onClick={() => openLesson(current - 1)}>← Previous Lesson</button>
                <button className="button primary" disabled={!lessonData?.next_unlocked || current >= 10 || busy} onClick={() => openLesson(current + 1)}>Next Lesson →</button>
              </div>
            </>}
            {!lesson && <p>Loading lesson…</p>}
          </section>
          <aside className="sidebar">
            <section className="panel"><p className="eyebrow">YOUR PROGRESS</p><h2>Keep your momentum</h2>
              <div className="count">{completedCount}<span> / 10</span></div><div className="progress-track"><span style={{ width: `${percent}%` }} /></div><p className="muted">{percent}% complete</p></section>
            <section className="panel"><p className="eyebrow">LITTLE WINS</p><h2>Achievements</h2>
              <div className="achievements">{Object.entries(achievements).map(([key, earned]) => <div className={`achievement${earned ? " earned" : ""}`} key={key}><span>{earned ? "✓" : "○"}</span><div><strong>{key.replaceAll("_", " ")}</strong></div></div>)}</div>
            </section>
            <section className="panel quests-panel"><p className="eyebrow">YOUR NEXT MILESTONES</p><h2>Quests</h2>
              <p className="muted">Quest completion tracking will be connected next.</p>
              {questTitles.map((q, i) => <p key={i}>{completedQuests.includes(i) ? "✓" : "○"} {q}</p>)}
            </section>
          </aside>
        </div>
      </>}
      {showPopup && <div role="presentation" style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,.65)", display: "grid", placeItems: "center", zIndex: 1000, padding: 16 }}>
        <section role="dialog" aria-modal="true" aria-labelledby="skill-modal-title" className="skill-card" style={{ background: "white", borderRadius: 16, padding: 28, maxWidth: 460, width: "100%" }}>
          <h2 id="skill-modal-title">What's your {hobbyName.toLowerCase()} experience?</h2>
          <p className="muted">Choose once to set your starting lesson.</p>
          <div className="skill-options">{["Beginner", "Intermediate", "Expert"].map((level) => <label key={level} className={`skill-option${selectedSkill === level ? " selected" : ""}`}>
            <input type="radio" name="skill" checked={selectedSkill === level} onChange={() => setSelectedSkill(level)} />
            <span><strong>{level}</strong><small>{skillDescriptions[level]}</small></span>
          </label>)}</div>
          <button className="button primary" disabled={!selectedSkill || busy} onClick={chooseSkill}>{busy ? "Loading…" : "Start my roadmap →"}</button>
        </section>
      </div>}
    </main>
  );
}

// For reading-only lessons that fit entirely in the scroll container, show an explicit
// end-of-reading action rather than marking the lesson complete merely on page load.
function ReadingEndObserver({ onReached }) {
  return <button className="button light" type="button" onClick={onReached}>I've reached the end of this short reading</button>;
}
