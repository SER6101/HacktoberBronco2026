import { useEffect, useRef, useState } from "react";
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
  const [loadingMore, setLoadingMore] = useState(false);
  const [error, setError] = useState("");
  const [catalogError, setCatalogError] = useState("");
  const requestedBatches = useRef(new Set());

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
  const ownedHobbies = new Set(user.hobbies || []);
  const batchPersonalized = (recommendations?.personalized || []).slice(0, 3);
  const personalized = batchPersonalized.filter((item) => !ownedHobbies.has(item.hobby));
  const personalizedNames = new Set(personalized.map((item) => item.hobby));
  const randomRecommendation = recommendations?.random;
  const hasNewRandomRecommendation = randomRecommendation
    && !ownedHobbies.has(randomRecommendation.hobby)
    && !personalizedNames.has(randomRecommendation.hobby);
  const recommended = [
    ...personalized,
    ...(hasNewRandomRecommendation ? [randomRecommendation] : []),
  ];
  const recommendedNames = new Set(recommended.map((item) => item.hobby));
  const previouslyRecommendedNames = new Set([
    ...(recommendations?.personalized || []).map((item) => item.hobby),
    ...(recommendations?.random ? [recommendations.random.hobby] : []),
  ]);
  const excludedHobbies = [...new Set([
    ...ownedHobbies,
    ...previouslyRecommendedNames,
  ])].sort();
  const excludedKey = excludedHobbies.join("|");
  const visible = showAll
    ? catalog.filter((item) =>
      !ownedHobbies.has(item.hobby) && !recommendedNames.has(item.hobby))
    : [];
  const selectedHobby = selectedHobbies[0] || "";
  const allPersonalizedOwned = batchPersonalized.length > 0
    && batchPersonalized.every((item) => ownedHobbies.has(item.hobby));

  function renderHobbyCard(item, isRandom = false) {
    const hobby = localHobbies.find((entry) => entry.name === item.hobby);
    const isSelected = selectedHobby === item.hobby;
    return (
      <button
        key={item.hobby}
        type="button"
        className={`pick-card${isSelected ? " selected" : ""}${isRandom ? " random-pick-card" : ""}`}
        aria-pressed={isSelected}
        onClick={() => onToggle(item.hobby)}
      >
        <span className="hobby-icon">{hobby?.icon || "✦"}</span>
        <span className="check">{isSelected ? "✓" : ""}</span>
        <small className={isRandom ? "random-pick-label" : undefined}>
          {isRandom ? "TRY SOMETHING NEW" : hobby?.category || "HOBBY"}
        </small>
        <strong>{item.hobby}</strong>
        <span className="description">{item.description || hobby?.description}</span>
        {isSelected && <span className="selected-label">Selected</span>}
      </button>
    );
  }

  useEffect(() => {
    if (!startAtPicker || phase !== "picker" || showAll || catalog.length === 0
      || !allPersonalizedOwned || !catalog.some((item) => !ownedHobbies.has(item.hobby))
      || requestedBatches.current.has(excludedKey)) return undefined;

    requestedBatches.current.add(excludedKey);
    let active = true;
    setLoadingMore(true);
    setError("");

    submitQuestionnaire(answers, excludedHobbies)
      .then((result) => {
        if (!active) return;
        if (onSaveAnswers(answers, result.recommendations)) {
          setRecommendations(result.recommendations);
        } else {
          setError("Could not save the new recommendations. Please try again.");
        }
      })
      .catch((err) => {
        if (active) setError(err.message);
      })
      .finally(() => {
        if (active) setLoadingMore(false);
      });

    return () => { active = false; };
  }, [startAtPicker, phase, showAll, catalog.length, allPersonalizedOwned, excludedKey]);

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
      <section className="page-heading"><p className="eyebrow">YOUR HOBBY SHORTLIST</p><h1>Choose one hobby to get started.</h1><p>Choose a new recommendation or browse other hobbies you haven’t added yet.</p></section>
      {!showAll && <p className="picker-section-label">RECOMMENDED FOR YOU <span>{personalized.length} personalized picks</span></p>}
      {showAll && <p className="picker-section-label">EXPLORE OTHER HOBBIES</p>}
      {showAll ? (
        <div className="picker-grid">{visible.map((item) => renderHobbyCard(item))}</div>
      ) : (
        <>
          {personalized.length > 0
            ? <div className="picker-grid">{personalized.map((item) => renderHobbyCard(item))}</div>
            : <p className="muted" role={loadingMore ? "status" : undefined}>
              {loadingMore ? "Finding more personalized hobbies…" : "No more personalized hobbies match your answers."}
            </p>}
          {hasNewRandomRecommendation && (
            <section className="random-pick-section" aria-label="Try something new">
              <div>
                <p className="picker-section-label">TRY SOMETHING NEW</p>
                <p className="muted">A random pick outside your personalized recommendations.</p>
              </div>
              <div className="picker-grid random-pick-grid">
                {renderHobbyCard(randomRecommendation, true)}
              </div>
            </section>
          )}
        </>
      )}
      <div className="picker-more-actions">
        {!showAll && <button type="button" className="button light" onClick={() => setShowAll(true)}>Show other hobbies →</button>}
        {showAll && <button type="button" className="text-button back-to-picks" onClick={() => setShowAll(false)}>← Back to recommendations</button>}
      </div>
      {!showAll && personalized.length === 0 && !loadingMore
        && !hasNewRandomRecommendation && <p className="muted">Try exploring other hobbies.</p>}
      {(error || catalogError) && <p className="error" role="alert">{error || catalogError}</p>}
      <div className="sticky-action"><span>{selectedHobby ? `${selectedHobby} selected` : "Choose one hobby to continue"}</span><button className="button primary" disabled={!selectedHobby} onClick={onSaveHobbies}>Save to my page →</button></div>
    </main>
  );
}
