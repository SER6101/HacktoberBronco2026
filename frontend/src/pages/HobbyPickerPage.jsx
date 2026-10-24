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
  const [showAll, setShowAll] = useState(false);
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
  const personalized = (recommendations?.personalized || []).slice(0, 3);
  const personalizedNames = new Set(personalized.map((item) => item.hobby));
  const recommended = [
    ...personalized,
    ...(recommendations?.random && !personalizedNames.has(recommendations.random.hobby)
      ? [recommendations.random]
      : []),
  ];
  const recommendedNames = new Set(recommended.map((item) => item.hobby));
  const visible = showAll
    ? catalog.filter((item) => !recommendedNames.has(item.hobby))
    : recommended;
  const selectedHobby = selectedHobbies[0] || "";

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
      <section className="page-heading"><p className="eyebrow">YOUR HOBBY SHORTLIST</p><h1>Choose one hobby to get started.</h1><p>Here are three recommendations based on your answers and one random pick.</p></section>
      {!showAll && <p className="picker-section-label">RECOMMENDED FOR YOU <span>3 personalized picks + 1 random pick</span></p>}
      {showAll && <p className="picker-section-label">EXPLORE OTHER HOBBIES</p>}
      <div className="picker-grid">{visible.map((item) => {
        const hobby = localHobbies.find((h) => h.name === item.hobby);
        const isRandom = recommendations?.random?.hobby === item.hobby;
        return <button key={item.hobby} type="button" className={`pick-card${selectedHobby === item.hobby ? " selected" : ""}`}
          aria-pressed={selectedHobby === item.hobby} onClick={() => onToggle(item.hobby)}>
          <span className="hobby-icon">{hobby?.icon || "✦"}</span><span className="check">{selectedHobby === item.hobby ? "✓" : ""}</span>
          <small className={isRandom && !showAll ? "random-pick-label" : undefined}>
            {isRandom && !showAll ? "TRY SOMETHING NEW" : hobby?.category || "HOBBY"}
          </small>
          <strong>{item.hobby}</strong><span className="description">{item.description || hobby?.description}</span>
          {selectedHobby === item.hobby && <span className="selected-label">Selected</span>}
        </button>;
      })}</div>
      <div className="picker-more-actions">
        {!showAll && <button type="button" className="button light" onClick={() => setShowAll(true)}>Show other hobbies →</button>}
        {showAll && <button type="button" className="text-button back-to-picks" onClick={() => setShowAll(false)}>← Back to recommendations</button>}
      </div>
      {!showAll && recommended.length === 0 && <p className="error" role="alert">Recommendations aren’t available yet. Try exploring the full hobby list.</p>}
      {(error || catalogError) && <p className="error" role="alert">{error || catalogError}</p>}
      <div className="sticky-action"><span>{selectedHobby ? `${selectedHobby} selected` : "Choose one hobby to continue"}</span><button className="button primary" disabled={!selectedHobby} onClick={onSaveHobbies}>Save to my page →</button></div>
    </main>
  );
}
