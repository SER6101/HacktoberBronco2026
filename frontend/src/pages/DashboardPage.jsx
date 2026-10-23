import { hobbies } from "../data/hobbies.js";

export default function DashboardPage({ user, onOpenHobby, onAddHobbies, onSignOut }) {
  return (
    <main className="wide">
      <div className="topline"><span>Your little corner for learning and doing.</span><button className="text-button" onClick={onSignOut}>Sign out</button></div>
      <section className="welcome"><div><p className="eyebrow">YOUR HOBOBB PAGE</p><h1>Welcome back, {user.name.split(" ")[0]}.</h1><p>Every expert starts somewhere. Pick a hobby to continue your journey.</p></div><div className="stamp">MAKE TIME<br /><em>FOR YOU</em></div></section>
      <div className="section-title"><div><p className="eyebrow">YOUR COLLECTION</p><h2>Hobbies you’re exploring</h2></div><button className="button light" onClick={onAddHobbies}>＋ Add hobbies</button></div>
      {user.hobbies.length
        ? <div className="dashboard-grid">{user.hobbies.map((name) => {
          const hobby = hobbies.find((item) => item.name === name);
          const count = user.progress?.[name]?.length || 0;
          return <button className="dashboard-hobby" key={name} onClick={() => onOpenHobby(name)}><span className="dashboard-icon">{hobby?.icon}</span><span className="dashboard-copy"><strong>{name}</strong><small>{count ? `${count} of 5 steps complete` : "Ready when you are · Start with step one"}</small></span><span className="arrow">→</span></button>;
        })}</div>
        : <div className="empty"><span>✳</span><h2>Your next favorite thing is out there.</h2><p>Choose a few hobbies and we’ll make a learning path for each one.</p><button className="button primary" onClick={onAddHobbies}>Explore hobbies <span>→</span></button></div>}
    </main>
  );
}
