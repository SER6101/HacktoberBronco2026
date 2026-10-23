import { useEffect, useState } from "react";
import { hobbies } from "../data/hobbies.js";
import { getProgress } from "../services/api.js";

export default function DashboardPage({ user, sessionId, onOpenHobby, onAddHobbies, onSignOut }) {
  const [counts, setCounts] = useState({});
  useEffect(() => {
    let active = true;
    Promise.all((user.hobbies || []).map(async (name) => {
      const skill = user.skillLevels?.[name];
      if (!skill) return [name, null];
      try { const data = await getProgress(name, skill, sessionId); return [name, data.progress.completed]; }
      catch { return [name, null]; }
    })).then((pairs) => { if (active) setCounts(Object.fromEntries(pairs)); });
    return () => { active = false; };
  }, [user.hobbies, user.skillLevels, sessionId]);

  return <main className="wide">
    <div className="topline"><span>Your little corner for learning and doing.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
    <section className="welcome"><div><p className="eyebrow">YOUR HOBBOB PAGE</p><h1>Welcome back, {user.name.split(" ")[0]}.</h1><p>Every expert starts somewhere. Pick a hobby to continue your journey.</p></div><div className="stamp">MAKE TIME<br /><em>FOR YOU</em></div></section>
    <div className="section-title"><div><p className="eyebrow">YOUR COLLECTION</p><h2>Hobbies you’re exploring</h2></div><button className="button light" onClick={onAddHobbies}>＋ Add hobbies</button></div>
    {(user.hobbies || []).length ? <div className="dashboard-grid">{user.hobbies.map((name) => {
      const hobby = hobbies.find((item) => item.name === name);
      const count = counts[name];
      return <button className="dashboard-hobby" key={name} onClick={() => onOpenHobby(name)}>
        <span className="dashboard-icon">{hobby?.icon || "✦"}</span><span className="dashboard-copy"><strong>{name}</strong>
        <small>{count === null || count === undefined ? "Ready to start your roadmap" : `${count} of 10 lessons complete`}</small></span><span className="arrow">→</span>
      </button>;
    })}</div> : <div className="empty"><span>✳</span><h2>Your next favorite thing is out there.</h2><p>Choose a few hobbies and we’ll make a learning path for each one.</p><button className="button primary" onClick={onAddHobbies}>Explore hobbies →</button></div>}
  </main>;
}
