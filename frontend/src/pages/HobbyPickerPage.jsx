import { useState } from "react";
import { hobbies, questions } from "../data/hobbies.js";

export default function HobbyPickerPage({
  user,
  selectedHobbies,
  onToggle,
  onSaveAnswers,
  onSaveHobbies,
  onBack,
  onSignOut,
  startAtPicker = false,
}) {
  const [phase, setPhase] = useState(startAtPicker ? "picker" : "questionnaire");
  const [questionIndex, setQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState(user.answers || Array(questions.length).fill(""));
  const question = questions[questionIndex];

  if (phase === "questionnaire") {
    return (
      <main className="narrow">
        <div className="topline"><span>Hi {user.name.split(" ")[0]}, let’s find your kind of fun.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
        <section className="quiz-card">
          <p className="eyebrow">A FEW QUICK QUESTIONS</p>
          <div className="progress-track"><span style={{ width: `${(questionIndex + 1) / questions.length * 100}%` }} /></div>
          <p className="step-label">QUESTION {questionIndex + 1} OF {questions.length}</p>
          <h1>{question.prompt}</h1>
          <div className="choices">
            {question.choices.map((choice) => (
              <label className={`choice${answers[questionIndex] === choice ? " selected" : ""}`} key={choice}>
                <input type="radio" name={`q-${questionIndex}`} checked={answers[questionIndex] === choice} onChange={() => setAnswers((previous) => previous.map((answer, index) => index === questionIndex ? choice : answer))} />
                {choice}<span className="radio" />
              </label>
            ))}
          </div>
          <div className="actions">
            {questionIndex > 0 && <button className="button light" type="button" onClick={() => setQuestionIndex(questionIndex - 1)}>← Back</button>}
            {questionIndex < questions.length - 1
              ? <button className="button primary" type="button" disabled={!answers[questionIndex]} onClick={() => setQuestionIndex(questionIndex + 1)}>Next question <span>→</span></button>
              : <button className="button primary" type="button" disabled={!answers[questionIndex]} onClick={() => {
                if (onSaveAnswers(answers)) setPhase("picker");
              }}>Choose my hobbies <span>→</span></button>}
          </div>
        </section>
        <p className="center muted">No wrong answers. This just helps us get started.</p>
      </main>
    );
  }

  return (
    <main className="wide">
      <div className="topline"><button className="text-button back" onClick={startAtPicker ? onBack : () => setPhase("questionnaire")}>{startAtPicker ? "← My hobbies" : "← Back to questions"}</button><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="page-heading"><p className="eyebrow">YOUR HOBBY SHORTLIST</p><h1>What would you like to try?</h1><p>Choose as many as you like. Each one becomes its own learning path.</p></section>
      <div className="picker-grid">
        {hobbies.map((hobby) => (
          <button key={hobby.name} className={`pick-card${selectedHobbies.includes(hobby.name) ? " selected" : ""}`} aria-pressed={selectedHobbies.includes(hobby.name)} onClick={() => onToggle(hobby.name)}>
            <span className="hobby-icon">{hobby.icon}</span><span className="check">{selectedHobbies.includes(hobby.name) ? "✓" : "+"}</span>
            <small>{hobby.category}</small><strong>{hobby.name}</strong><span className="description">{hobby.description}</span>
          </button>
        ))}
      </div>
      <div className="sticky-action"><span>{selectedHobbies.length} {selectedHobbies.length === 1 ? "hobby" : "hobbies"} selected</span><button className="button primary" disabled={!selectedHobbies.length} onClick={onSaveHobbies}>Save to my page <span>→</span></button></div>
    </main>
  );
}
