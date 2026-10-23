import { useState } from "react";
import { hobbies, skillDescriptions, skillRoadmaps } from "../data/hobbies.js";

export default function HobbyProgressPage({ user, hobbyName, onBack, onCompleteStep, onSaveSkill }) {
  const hobby = hobbies.find((item) => item.name === hobbyName);
  const completed = user.progress?.[hobbyName] || [];
  const skill = user.skillLevels?.[hobbyName];
  const [isChoosingSkill, setIsChoosingSkill] = useState(!skill);
  const [selectedSkill, setSelectedSkill] = useState(skill || "");
  const [step, setStep] = useState(null);
  const [isRoadmapExpanded, setIsRoadmapExpanded] = useState(true);
  const activeRoadmap = skillRoadmaps[skill] || skillRoadmaps.Beginner;
  const selectedCheckpoint = step === null ? null : activeRoadmap[step];
  const percent = Math.round(completed.length / activeRoadmap.length * 100);
  const unlocked = Math.min(completed.length + 1, activeRoadmap.length);
  const achievements = [
    ["First step", "Complete your first checkpoint.", completed.length >= 1],
    ["Finding your rhythm", "Complete three checkpoints.", completed.length >= 3],
    ["Path maker", "Finish every checkpoint.", completed.length === activeRoadmap.length],
  ];
  const quests = activeRoadmap.slice(0, 3).map(([checkpointName], index) => ({
    title: `Reach ${checkpointName.toLowerCase()}`,
    completed: completed.includes(index),
    checkpoint: index + 1,
  }));
  const earnedAchievements = achievements.filter(([, , earned]) => earned);
  const completedQuests = quests.filter((quest) => quest.completed);

  if (isChoosingSkill) {
    return (
      <main className="wide">
        <button className="text-button back" onClick={onBack}>← My hobbies</button>
        <section className="skill-card">
          <span className="big-icon">{hobby?.icon}</span>
          <p className="eyebrow">PERSONALIZE YOUR ROADMAP</p>
          <h1>What’s your {hobbyName.toLowerCase()} experience?</h1>
          <p className="muted">We’ll use this to choose the right starting point and tutorials. You can change it later.</p>
          <div className="skill-options">
            {Object.entries(skillDescriptions).map(([level, description]) => (
              <label className={`skill-option${selectedSkill === level ? " selected" : ""}`} key={level}>
                <input type="radio" name={`skill-${hobbyName}`} value={level} checked={selectedSkill === level} onChange={() => setSelectedSkill(level)} />
                <span><strong>{level}</strong><small>{description}</small></span>
                <span className="radio" />
              </label>
            ))}
          </div>
          <div className="skill-actions">
            {skill && <button className="button light" type="button" onClick={() => setIsChoosingSkill(false)}>Cancel</button>}
            <button className="button primary" type="button" disabled={!selectedSkill} onClick={() => {
              if (onSaveSkill(hobbyName, selectedSkill)) {
                setIsChoosingSkill(false);
                setStep(null);
                setIsRoadmapExpanded(true);
              }
            }}>Start my roadmap <span>→</span></button>
          </div>
        </section>
      </main>
    );
  }

  return (
    <main className="wide">
      <button className="text-button back" onClick={onBack}>← My hobbies</button>
      <section className="progress-heading">
        <span className="big-icon">{hobby?.icon}</span>
        <div className="hobby-heading">
          <p className="eyebrow">{hobby?.category} · {skill} ROADMAP</p>
          <h1>{hobbyName}</h1>
          <p>{hobby?.description}</p>
          <button className="text-button change-skill" type="button" onClick={() => { setSelectedSkill(skill); setIsChoosingSkill(true); }}>Change skill level</button>
        </div>
        <div className="progress-summary"><strong>{percent}%</strong><small>journey complete</small><div className="progress-track"><span style={{ width: `${percent}%` }} /></div></div>
      </section>
      <div className="learning-layout">
        <section className="panel">
          <div className="panel-heading"><div><p className="eyebrow">ONE STEP AT A TIME</p><h2>Your learning roadmap</h2></div><small>{completed.length}/{activeRoadmap.length} done</small></div>
          {!completed.length && !selectedCheckpoint && <div className="first-step"><strong>✦ &nbsp;Take your first step!</strong><p>Choose a checkpoint below to open its {skill.toLowerCase()}-friendly tutorial.</p></div>}
          {isRoadmapExpanded ? (
            <div className="roadmap">{activeRoadmap.map(([title, duration], index) => {
              const done = completed.includes(index);
              const canOpen = index < unlocked;
              return (
                <button key={title} className={`roadmap-step${step === index ? " active" : ""}${done ? " done" : ""}`} disabled={!canOpen} onClick={() => { setStep(index); setIsRoadmapExpanded(false); }}>
                  <span className="marker">{done ? "✓" : String(index + 1).padStart(2, "0")}</span>
                  <span className="roadmap-copy"><strong>{title}</strong><small>{duration} · {done ? "Completed" : canOpen ? "Ready to explore" : "Complete the previous step to unlock"}</small></span>
                </button>
              );
            })}</div>
          ) : selectedCheckpoint && (
            <button className="selected-checkpoint" type="button" onClick={() => setIsRoadmapExpanded(true)} aria-expanded="false">
              <span className="marker">{completed.includes(step) ? "✓" : String(step + 1).padStart(2, "0")}</span>
              <span className="roadmap-copy"><strong>{selectedCheckpoint[0]}</strong><small>Checkpoint {step + 1} · {selectedCheckpoint[1]}</small></span>
              <span className="selected-change">Change checkpoint</span>
            </button>
          )}
          {selectedCheckpoint && (
            <section className="checkpoint">
              <p className="eyebrow">CHECKPOINT {String(step + 1).padStart(2, "0")} · {selectedCheckpoint[1].toUpperCase()}</p>
              <h2>{selectedCheckpoint[0]}</h2>
              <p className="muted">{selectedCheckpoint[2]}</p>
              <div className="tutorial"><p className="eyebrow">YOUR TUTORIAL</p><p>{selectedCheckpoint[3].replaceAll("your hobby", hobbyName.toLowerCase())}</p></div>
              <div className="video"><span>▶</span><div><strong>Video lesson coming soon</strong><small>We’ll add a {hobbyName.toLowerCase()} video tutorial here.</small></div><small className="placeholder">PLACEHOLDER</small></div>
              {completed.includes(step)
                ? <p className="complete-msg">✓ &nbsp;Checkpoint complete — nice work!</p>
                : <button className="button primary complete" onClick={() => onCompleteStep(hobbyName, step)}>Mark checkpoint complete <span>✓</span></button>}
            </section>
          )}
        </section>
        <aside className="sidebar">
          <section className="panel"><p className="eyebrow">YOUR PROGRESS</p><h2>Keep your momentum</h2><div className="count">{completed.length}<span> / {activeRoadmap.length}</span></div><small className="muted">checkpoints complete</small><div className="progress-track"><span style={{ width: `${percent}%` }} /></div><p className="tip">{completed.length ? "Every little bit of practice counts. Come back when you’re ready for the next step." : "A few minutes is all it takes to begin. Your first checkpoint is ready."}</p></section>
          <section className="panel"><p className="eyebrow">LITTLE WINS</p><h2>Achievements</h2>
            {!earnedAchievements.length && !completedQuests.length ? (
              <div className="achievement-empty"><span>✦</span><p>Your first achievement is waiting!</p><small>Complete a quest or checkpoint to see it here.</small></div>
            ) : (
              <div className="achievements">
                {earnedAchievements.map(([title, detail]) => <div className="achievement earned" key={title}><span>✦</span><div><strong>{title}</strong><small>{detail}</small></div><b>✓</b></div>)}
                {completedQuests.map((quest) => <div className="achievement earned" key={quest.title}><span>✓</span><div><strong>{quest.title}</strong><small>Quest complete · Checkpoint {quest.checkpoint}</small></div><b>✓</b></div>)}
              </div>
            )}
          </section>
          <section className="panel quests-panel">
            <p className="eyebrow">YOUR NEXT MILESTONES</p><h2>Quests</h2>
            {quests.every((quest) => quest.completed) ? (
              <div className="achievement-empty"><span>✦</span><p>All quests complete!</p><small>Keep going on your roadmap to unlock more achievements.</small></div>
            ) : (
              <div className="quests-list">{quests.filter((quest) => !quest.completed).map((quest) => (
                <div className="quest" key={quest.title}><span className="quest-marker">{String(quest.checkpoint).padStart(2, "0")}</span><span className="quest-copy"><strong>{quest.title}</strong><small>Complete checkpoint {quest.checkpoint}</small></span></div>
              ))}</div>
            )}
          </section>
        </aside>
      </div>
    </main>
  );
}
