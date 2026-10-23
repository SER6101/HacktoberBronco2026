import { useState } from "react";

export default function AuthPage({ onSignup, onLogin }) {
  const [mode, setMode] = useState("signup");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  function submit(event) {
    event.preventDefault();
    setError("");
    if (mode === "signup" && !name.trim()) {
      setError("Enter your name to create a demo profile.");
      return;
    }
    try {
      if (mode === "signup") onSignup({ name: name.trim(), email: email.trim().toLowerCase() });
      else onLogin(email.trim().toLowerCase());
    } catch (submitError) {
      setError(submitError.message || "Could not sign in. Please try again.");
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
          <button className={mode === "signup" ? "active" : ""} onClick={() => { setMode("signup"); setError(""); }} type="button">Create account</button>
          <button className={mode === "login" ? "active" : ""} onClick={() => { setMode("login"); setError(""); }} type="button">Log in</button>
        </div>
        <p className="eyebrow">{mode === "signup" ? "YOUR JOURNEY STARTS HERE" : "WELCOME BACK"}</p>
        <h2>{mode === "signup" ? "Let’s get to know you." : "Pick up where you left off."}</h2>
        <p className="muted">{mode === "signup" ? "Create a demo profile, then we’ll find hobbies to explore." : "Log in to see your saved hobbies and progress."}</p>
        <form onSubmit={submit} className="auth-form">
          {mode === "signup" && <label>Your name<input value={name} onChange={(event) => setName(event.target.value)} placeholder="Alex Morgan" /></label>}
          <label>Email address<input type="email" required value={email} onChange={(event) => setEmail(event.target.value)} placeholder="you@example.com" /></label>
          <label>Password<input type="password" required minLength={6} value={password} onChange={(event) => setPassword(event.target.value)} placeholder="At least 6 characters" /></label>
          {error && <p className="error" role="alert">{error}</p>}
          <button className="button primary wide">{mode === "signup" ? "Create account" : "Log in"} <span>→</span></button>
        </form>
        <p className="fine-print">Demo only: profiles are stored in this browser. Passwords are not stored; this is not secure authentication.</p>
      </section>
    </main>
  );
}
