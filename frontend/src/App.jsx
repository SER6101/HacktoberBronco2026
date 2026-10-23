import { useState } from "react";

const questions = [
  { prompt: "What would you like a hobby to bring to your life?", choices: ["A chance to relax", "A new skill", "More movement", "A creative outlet"] },
  { prompt: "How do you like to spend your free time?", choices: ["Making things", "Exploring", "Solving problems", "Being active"] },
  { prompt: "What kind of setting sounds good?", choices: ["On my own", "With a small group", "Meeting new people", "A bit of everything"] },
];

const hobbies = [
  { name: "Drawing", category: "Creative", icon: "✎", description: "Practice sketching and bring your ideas to life." },
  { name: "Hiking", category: "Outdoors", icon: "⌁", description: "Find new trails and enjoy time outside." },
  { name: "Cooking", category: "Creative", icon: "◒", description: "Build kitchen confidence one recipe at a time." },
  { name: "Photography", category: "Creative", icon: "◉", description: "Learn to notice and capture the little details." },
  { name: "Gardening", category: "Outdoors", icon: "❋", description: "Grow something green, from herbs to flowers." },
  { name: "Playing Guitar", category: "Music", icon: "♫", description: "Learn chords and play songs you love." },
  { name: "Chess", category: "Strategy", icon: "♞", description: "Explore patterns, tactics, and thoughtful play." },
  { name: "Pottery", category: "Creative", icon: "◡", description: "Shape clay into useful and beautiful objects." },
  { name: "Cycling", category: "Movement", icon: "⟲", description: "Build confidence and explore on two wheels." },
];

const roadmap = [
  ["Take your first step", "10 min", "Set up a small, welcoming space to begin.", "Start simple: gather what you already have, pick one tiny goal, and give yourself permission to learn as you go."],
  ["Learn the foundations", "20 min", "Get to know the core tools, terms, and techniques.", "Choose one beginner-friendly technique and practice it slowly. Repetition builds confidence more than getting it perfect."],
  ["Practice a little", "30 min", "Try a short practice session and notice what you enjoy.", "Set a timer for a short session. Focus on the process, and jot down one thing you learned afterward."],
  ["Make your first project", "45 min", "Bring the pieces together in a small project you can finish.", "Pick a project that fits in one session. Keep the goal achievable and make it your own as you work."],
  ["Find your own style", "Ongoing", "Keep exploring, try a new challenge, and choose what to learn next.", "Look back at what you enjoyed most. Use that as a guide for choosing your next skill, project, or community."],
];

const ACCOUNTS = "hobbob.demo.accounts";
const ACTIVE = "hobbob.demo.active";

function loadAccounts() {
  return JSON.parse(localStorage.getItem(ACCOUNTS) || "{}");
}

function Brand() {
  return <a className="brand" href="/" onClick={(event) => event.preventDefault()}><span className="brand-mark">h.</span>HobBob</a>;
}

function Auth({ onSignup, onLogin }) {
  const [mode, setMode] = useState("signup");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  function submit(event) {
    event.preventDefault();
    setError("");
    const normalized = email.trim().toLowerCase();
    const accounts = loadAccounts();
    if (mode === "signup") {
      if (!name.trim()) return setError("Enter your name to create a demo profile.");
      if (accounts[normalized]) return setError("That email already has a demo profile. Try logging in.");
      onSignup({ name: name.trim(), email: normalized });
    } else if (accounts[normalized]) {
      onLogin(accounts[normalized]);
    } else {
      setError("No demo profile found for that email. Create an account first.");
    }
  }

  return (
    <main className="auth-layout">
      <section className="auth-story">
        <p className="eyebrow">A LITTLE TIME FOR YOU</p>
        <h1>Make room for<br /><em>something new.</em></h1>
        <p>Discover a hobby, follow a friendly roadmap, and celebrate every little step along the way.</p>
        <div className="story-note">✳ &nbsp;Your progress, your pace. Always.</div>
      </section>
      <section className="auth-card">
        <div className="tabs">
          <button className={mode === "signup" ? "active" : ""} onClick={() => { setMode("signup"); setError(""); }}>Create account</button>
          <button className={mode === "login" ? "active" : ""} onClick={() => { setMode("login"); setError(""); }}>Log in</button>
        </div>
        <p className="eyebrow">{mode === "signup" ? "YOUR JOURNEY STARTS HERE" : "WELCOME BACK"}</p>
        <h2>{mode === "signup" ? "Let’s get to know you." : "Pick up where you left off."}</h2>
        <p className="muted">{mode === "signup" ? "Create a demo profile, then we’ll find hobbies to explore." : "Log in to see your saved hobbies and progress."}</p>
        <form onSubmit={submit} className="auth-form">
          {mode === "signup" && <label>Your name<input value={name} onChange={(e) => setName(e.target.value)} placeholder="Alex Morgan" /></label>}
          <label>Email address<input type="email" required value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com" /></label>
          <label>Password<input type="password" required minLength={6} value={password} onChange={(e) => setPassword(e.target.value)} placeholder="At least 6 characters" /></label>
          {error && <p className="error" role="alert">{error}</p>}
          <button className="button primary wide">{mode === "signup" ? "Create account" : "Log in"} <span>→</span></button>
        </form>
        <p className="fine-print">Demo only: profiles are stored in this browser. Passwords are not stored; this is not secure authentication.</p>
      </section>
    </main>
  );
}

function Questionnaire({ name, onFinish, onSignOut }) {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState(Array(questions.length).fill(""));
  const question = questions[step];
  return (
    <main className="narrow">
      <div className="topline"><span>Hi {name}, let’s find your kind of fun.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="quiz-card">
        <p className="eyebrow">A FEW QUICK QUESTIONS</p>
        <div className="progress-track"><span style={{ width: `${(step + 1) / questions.length * 100}%` }} /></div>
        <p className="step-label">QUESTION {step + 1} OF {questions.length}</p>
        <h1>{question.prompt}</h1>
        <div className="choices">
          {question.choices.map((choice) => (
            <label className={`choice${answers[step] === choice ? " selected" : ""}`} key={choice}>
              <input type="radio" name={`q-${step}`} checked={answers[step] === choice} onChange={() => setAnswers((old) => old.map((answer, index) => index === step ? choice : answer))} />
              {choice}<span className="radio" />
            </label>
          ))}
        </div>
        <div className="actions">
          {step > 0 && <button className="button light" onClick={() => setStep(step - 1)}>← Back</button>}
          {step < questions.length - 1
            ? <button className="button primary" disabled={!answers[step]} onClick={() => setStep(step + 1)}>Next question <span>→</span></button>
            : <button className="button primary" disabled={!answers[step]} onClick={() => onFinish(answers)}>Choose my hobbies <span>→</span></button>}
        </div>
      </section>
      <p className="center muted">No wrong answers. This just helps us get started.</p>
    </main>
  );
}

function HobbyPicker({ chosen, onToggle, onSave, onBack }) {
  return (
    <main className="wide">
      <button className="text-button back" onClick={onBack}>← Back to questions</button>
      <section className="page-heading"><p className="eyebrow">YOUR HOBBY SHORTLIST</p><h1>What would you like to try?</h1><p>Choose as many as you like. Each one becomes its own learning path.</p></section>
      <div className="picker-grid">
        {hobbies.map((hobby) => (
          <button key={hobby.name} className={`pick-card${chosen.includes(hobby.name) ? " selected" : ""}`} aria-pressed={chosen.includes(hobby.name)} onClick={() => onToggle(hobby.name)}>
            <span className="hobby-icon">{hobby.icon}</span><span className="check">{chosen.includes(hobby.name) ? "✓" : "+"}</span>
            <small>{hobby.category}</small><strong>{hobby.name}</strong><span className="description">{hobby.description}</span>
          </button>
        ))}
      </div>
      <div className="sticky-action"><span>{chosen.length} {chosen.length === 1 ? "hobby" : "hobbies"} selected</span><button className="button primary" disabled={!chosen.length} onClick={onSave}>Save to my page <span>→</span></button></div>
    </main>
  );
}

function Dashboard({ user, onOpen, onAdd, onSignOut }) {
  return (
    <main className="wide">
      <div className="topline"><span>Your little corner for learning and doing.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="welcome"><div><p className="eyebrow">YOUR HOBOBB PAGE</p><h1>Welcome back, {user.name.split(" ")[0]}.</h1><p>Every expert starts somewhere. Pick a hobby to continue your journey.</p></div><div className="stamp">MAKE TIME<br /><em>FOR YOU</em></div></section>
      <div className="section-title"><div><p className="eyebrow">YOUR COLLECTION</p><h2>Hobbies you’re exploring</h2></div><button className="button light" onClick={onAdd}>＋ Add hobbies</button></div>
      {user.hobbies.length
        ? <div className="dashboard-grid">{user.hobbies.map((name) => {
          const hobby = hobbies.find((item) => item.name === name);
          const count = user.progress?.[name]?.length || 0;
          return <button className="dashboard-hobby" key={name} onClick={() => onOpen(name)}><span className="dashboard-icon">{hobby?.icon}</span><span className="dashboard-copy"><strong>{name}</strong><small>{count ? `${count} of ${roadmap.length} steps complete` : "Ready when you are · Start with step one"}</small></span><span className="arrow">→</span></button>;
        })}</div>
        : <div className="empty"><span>✳</span><h2>Your next favorite thing is out there.</h2><p>Choose a few hobbies and we’ll make a learning path for each one.</p><button className="button primary" onClick={onAdd}>Explore hobbies <span>→</span></button></div>}
    </main>
  );
}

function HobbyProgress({ user, name, onBack, onComplete }) {
  const hobby = hobbies.find((item) => item.name === name);
  const completed = user.progress?.[name] || [];
  const [step, setStep] = useState(Math.min(completed.length, roadmap.length - 1));
  const [title, duration, description, tutorial] = roadmap[step];
  const percent = Math.round(completed.length / roadmap.length * 100);
  const unlocked = Math.min(completed.length + 1, roadmap.length);
  const achievements = [
    ["First step", "Complete your first checkpoint.", completed.length >= 1],
    ["Finding your rhythm", "Complete three checkpoints.", completed.length >= 3],
    ["Path maker", "Finish every checkpoint.", completed.length === roadmap.length],
  ];
  return (
    <main className="wide">
      <button className="text-button back" onClick={onBack}>← My hobbies</button>
      <section className="progress-heading"><span className="big-icon">{hobby?.icon}</span><div className="hobby-heading"><p className="eyebrow">{hobby?.category} · YOUR ROADMAP</p><h1>{name}</h1><p>{hobby?.description}</p></div><div className="progress-summary"><strong>{percent}%</strong><small>journey complete</small><div className="progress-track"><span style={{ width: `${percent}%` }} /></div></div></section>
      <div className="learning-layout">
        <section className="panel">
          <div className="panel-heading"><div><p className="eyebrow">ONE STEP AT A TIME</p><h2>Your learning roadmap</h2></div><small>{completed.length}/{roadmap.length} done</small></div>
          {!completed.length && <div className="first-step"><strong>✦ &nbsp;Take your first step!</strong><p>Pick a checkpoint to see a beginner-friendly tutorial. Start wherever feels right.</p></div>}
          <div className="roadmap">{roadmap.map(([stepName, time], index) => {
            const done = completed.includes(index);
            const canOpen = index < unlocked;
            return <button key={stepName} className={`roadmap-step${step === index ? " active" : ""}${done ? " done" : ""}`} disabled={!canOpen} onClick={() => setStep(index)}><span className="marker">{done ? "✓" : String(index + 1).padStart(2, "0")}</span><span className="roadmap-copy"><strong>{stepName}</strong><small>{time} · {done ? "Completed" : canOpen ? "Ready to explore" : "Complete the previous step to unlock"}</small></span></button>;
          })}</div>
          <section className="checkpoint"><p className="eyebrow">CHECKPOINT {String(step + 1).padStart(2, "0")} · {duration.toUpperCase()}</p><h2>{title}</h2><p className="muted">{description}</p><div className="tutorial"><p className="eyebrow">YOUR TUTORIAL</p><p>{tutorial.replaceAll("your hobby", name.toLowerCase())}</p></div><div className="video"><span>▶</span><div><strong>Video lesson coming soon</strong><small>We’ll add a {name.toLowerCase()} video tutorial here.</small></div><small className="placeholder">PLACEHOLDER</small></div>{completed.includes(step) ? <p className="complete-msg">✓ &nbsp;Checkpoint complete — nice work!</p> : <button className="button primary complete" onClick={() => onComplete(name, step)}>Mark checkpoint complete <span>✓</span></button>}</section>
        </section>
        <aside className="sidebar">
          <section className="panel"><p className="eyebrow">YOUR PROGRESS</p><h2>Keep your momentum</h2><div className="count">{completed.length}<span> / {roadmap.length}</span></div><small className="muted">checkpoints complete</small><div className="progress-track"><span style={{ width: `${percent}%` }} /></div><p className="tip">{completed.length ? "Every little bit of practice counts. Come back when you’re ready for the next step." : "A few minutes is all it takes to begin. Your first checkpoint is ready."}</p></section>
          <section className="panel"><p className="eyebrow">LITTLE WINS</p><h2>Achievements</h2><div className="achievements">{achievements.map(([achievement, detail, earned]) => <div className={`achievement${earned ? " earned" : ""}`} key={achievement}><span>{earned ? "✦" : "· · ·"}</span><div><strong>{achievement}</strong><small>{detail}</small></div>{earned && <b>✓</b>}</div>)}</div></section>
          <div className="placeholder-panel"><strong>Coming up</strong><p>Practice streaks and weekly goals will live here.</p><small>PLACEHOLDER</small></div>
        </aside>
      </div>
    </main>
  );
}

export default function App() {
  const [user, setUser] = useState(() => {
    try {
      const email = localStorage.getItem(ACTIVE);
      return email ? loadAccounts()[email] || null : null;
    } catch {
      return null;
    }
  });
  const [screen, setScreen] = useState(() => user ? user.answers ? "dashboard" : "questionnaire" : "auth");
  const [chosen, setChosen] = useState([]);

  function save(nextUser) {
    try {
      const accounts = loadAccounts();
      accounts[nextUser.email] = nextUser;
      localStorage.setItem(ACCOUNTS, JSON.stringify(accounts));
      localStorage.setItem(ACTIVE, nextUser.email);
      setUser(nextUser);
      return true;
    } catch {
      alert("Could not save the demo profile in browser storage.");
      return false;
    }
  }

  function signUp(profile) {
    if (save({ ...profile, answers: null, hobbies: [], progress: {} })) setScreen("questionnaire");
  }

  function logIn(account) {
    localStorage.setItem(ACTIVE, account.email);
    setUser(account);
    setScreen(account.answers ? "dashboard" : "questionnaire");
  }

  function finishQuestionnaire(answers) {
    const updated = { ...user, answers };
    if (save(updated)) {
      setChosen(updated.hobbies || []);
      setScreen("picker");
    }
  }

  function saveHobbies() {
    if (chosen.length && save({ ...user, hobbies: chosen, progress: user.progress || {} })) setScreen("dashboard");
  }

  function completeStep(name, index) {
    const previous = user.progress?.[name] || [];
    if (!previous.includes(index)) save({ ...user, progress: { ...user.progress, [name]: [...previous, index].sort((a, b) => a - b) } });
  }

  function signOut() {
    localStorage.removeItem(ACTIVE);
    setUser(null);
    setScreen("auth");
  }

  return <div className="app-shell">
    <header className="site-header"><Brand /><span>Small steps. New passions.{user && <b className="user-chip">{user.name}</b>}</span></header>
    {screen === "auth" && <Auth onSignup={signUp} onLogin={logIn} />}
    {screen === "questionnaire" && user && <Questionnaire name={user.name.split(" ")[0]} onFinish={finishQuestionnaire} onSignOut={signOut} />}
    {screen === "picker" && user && <HobbyPicker chosen={chosen} onToggle={(name) => setChosen((current) => current.includes(name) ? current.filter((item) => item !== name) : [...current, name])} onSave={saveHobbies} onBack={() => setScreen("questionnaire")} />}
    {screen === "dashboard" && user && <Dashboard user={user} onOpen={(name) => { setScreen(`hobby:${name}`); }} onAdd={() => { setChosen(user.hobbies || []); setScreen("picker"); }} onSignOut={signOut} />}
    {screen.startsWith("hobby:") && user && <HobbyProgress user={user} name={screen.slice(6)} onBack={() => setScreen("dashboard")} onComplete={completeStep} />}
    <footer className="site-footer"><strong>HobBob</strong><span>Make a little room for what you love.</span><small>DEMO EXPERIENCE</small></footer>
  </div>;
}
