import { useEffect, useState } from "react";
import { hobbies as localHobbies, questions } from "../data/hobbies.js";
import { getHobbies, submitQuestionnaire } from "../services/api.js";

export default function HobbyPickerPage({ user, selectedHobbies, onToggle, onSaveAnswers,
  onSaveHobbies, onBack, onSignOut, startAtPicker = false }) {
  const [phase, setPhase] = useState(startAtPicker ? "picker" : "questionnaire");
  const [catalog, setCatalog] = useState([]);
  const [questionIndex, setQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState(user.answers || Array(5).fill(""));
  const [recommendations, setRecommendations] = useState(user.recommendations || null);
  const [showAll, setShowAll] = useState(Boolean(startAtPicker));
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [catalogError, setCatalogError] = useState("");

  useEffect(() => {
    getHobbies()
      .then((result) => setCatalog(result.hobbies))
      .catch((err) => setCatalogError(err.message));
  }, []);

  async function finishQuestionnaire() {
    setBusy(true); setError("");
    try {
      const result = await submitQuestionnaire(answers);
      if (onSaveAnswers(answers, result.recommendations)) {
        setRecommendations(result.recommendations);
        setShowAll(false);
        setPhase("picker");
      }
    } catch (err) { setError(err.message); }
    finally { setBusy(false); }
  }

  const question = questions[questionIndex];
  const recommendedNames = [
    ...(recommendations?.personalized || []).map((h) => h.hobby),
    ...(recommendations?.random ? [recommendations.random.hobby] : []),
  ];
  const visible = showAll ? catalog : catalog.filter((h) => recommendedNames.includes(h.hobby));

  if (phase === "questionnaire") return (
    <main className="narrow">
      <div className="topline"><span>Hi {user.name.split(" ")[0]}, let’s find your kind of fun.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="quiz-card">
        <p className="eyebrow">A FEW QUICK QUESTIONS</p>
        <div className="progress-track"><span style={{ width: `${(questionIndex + 1) / questions.length * 100}%` }} /></div>
        <p className="step-label">QUESTION {questionIndex + 1} OF {questions.length}</p>
        {question ? <>
          <h1>{question.question}</h1>
          <div className="choices">{question.options.map((choice) => (
            <label className={`choice${answers[questionIndex] === choice ? " selected" : ""}`} key={choice}>
              <input type="radio" name={`q-${questionIndex}`} checked={answers[questionIndex] === choice}
                onChange={() => setAnswers((old) => old.map((v, i) => i === questionIndex ? choice : v))} />
              {choice}<span className="radio" />
            </label>
          ))}</div>
          <div className="actions">
            {questionIndex > 0 && <button className="button light" onClick={() => setQuestionIndex(questionIndex - 1)}>← Back</button>}
            {questionIndex < questions.length - 1
              ? <button className="button primary" disabled={!answers[questionIndex]} onClick={() => setQuestionIndex(questionIndex + 1)}>Next question →</button>
              : <button className="button primary" disabled={!answers[questionIndex] || busy} onClick={finishQuestionnaire}>{busy ? "Finding hobbies…" : "See my recommendations →"}</button>}
          </div>
        </> : null}
        {error && <p className="error" role="alert">{error}</p>}
      </section>
    </main>
  );

  return (
    <main className="wide">
      <div className="topline"><button className="text-button back" onClick={onBack}>← My hobbies</button><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="page-heading"><p className="eyebrow">YOUR HOBBY SHORTLIST</p><h1>What would you like to try?</h1><p>Select hobbies to add to your dashboard.</p></section>
      {!showAll && <p className="muted">Three personalized picks and one surprise suggestion.</p>}
      <div className="picker-grid">{visible.map((item) => {
        const hobby = localHobbies.find((h) => h.name === item.hobby);
        const isRandom = recommendations?.random?.hobby === item.hobby;
        return <button key={item.hobby} className={`pick-card${selectedHobbies.includes(item.hobby) ? " selected" : ""}`}
          aria-pressed={selectedHobbies.includes(item.hobby)} onClick={() => onToggle(item.hobby)}>
          <span className="hobby-icon">{hobby?.icon || "✦"}</span><span className="check">{selectedHobbies.includes(item.hobby) ? "✓" : "+"}</span>
          <small>{isRandom && !showAll ? "SURPRISE PICK" : hobby?.category || "HOBBY"}</small>
          <strong>{item.hobby}</strong><span className="description">{item.description}</span>
        </button>;
      })}</div>
      {!showAll && <button className="button light" onClick={() => setShowAll(true)}>Explore More Hobbies →</button>}
      {(error || catalogError) && <p className="error" role="alert">{error || catalogError}</p>}
      <div className="sticky-action"><span>{selectedHobbies.length} hobbies selected</span><button className="button primary" disabled={!selectedHobbies.length} onClick={onSaveHobbies}>Save to my page →</button></div>
    </main>
  );
}
