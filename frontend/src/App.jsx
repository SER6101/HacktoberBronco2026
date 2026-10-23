import { useState } from "react";
import Brand from "./components/Brand.jsx";
import AuthPage from "./pages/AuthPage.jsx";
import DashboardPage from "./pages/DashboardPage.jsx";
import HobbyPickerPage from "./pages/HobbyPickerPage.jsx";
import HobbyProgressPage from "./pages/HobbyProgressPage.jsx";
import {
  createDemoUser, getActiveUser, loginDemoUser, logoutDemoUser, saveDemoUser,
} from "./services/demoUserStore.js";

export default function App() {
  const [user, setUser] = useState(() => {
    try { return getActiveUser(); } catch { return null; }
  });
  const [screen, setScreen] = useState(() => !user ? "auth" : user.answers ? "dashboard" : "onboarding");
  const [selectedHobby, setSelectedHobby] = useState("");
  const [selectedHobbies, setSelectedHobbies] = useState([]);

  function saveUser(nextUser) {
    try { saveDemoUser(nextUser); setUser(nextUser); return true; }
    catch { window.alert("Could not save the demo profile in browser storage."); return false; }
  }
  function signUp(profile) {
    const newUser = createDemoUser(profile);
    setUser(newUser);
    setScreen("onboarding");
  }
  function logIn(email) {
    const existingUser = loginDemoUser(email);
    setUser(existingUser);
    setScreen(existingUser.answers ? "dashboard" : "onboarding");
  }
  function saveAnswers(answers, recommendations) {
    return user ? saveUser({ ...user, answers, recommendations }) : false;
  }
  function saveHobbies() {
    if (user && selectedHobbies.length && saveUser({
      ...user, hobbies: selectedHobbies,
      progress: user.progress || {}, skillLevels: user.skillLevels || {},
    })) setScreen("dashboard");
  }
  function saveSkillLevel(hobbyName, level) {
    return user ? saveUser({
      ...user, skillLevels: { ...user.skillLevels, [hobbyName]: level },
    }) : false;
  }
  function updateProgress(hobbyName, completedNumbers) {
    if (!user) return;
    saveUser({ ...user, progress: { ...user.progress, [hobbyName]: completedNumbers } });
  }
  function signOut() {
    try { logoutDemoUser(); }
    finally { setUser(null); setScreen("auth"); }
  }
  function beginOnboarding() {
    setSelectedHobbies(user?.hobbies || []);
    setScreen("onboarding");
  }

  // Stable demo identifier for SQLite; not authentication.
  const sessionId = user ? `hobbob-${user.email.trim().toLowerCase()}` : "";

  return (
    <div className="app-shell">
      <header className="site-header"><Brand /><span>Small steps. New passions.{user && <b className="user-chip">{user.name}</b>}</span></header>
      {screen === "auth" && <AuthPage onSignup={signUp} onLogin={logIn} />}
      {screen === "onboarding" && user && (
        <HobbyPickerPage user={user} selectedHobbies={selectedHobbies}
          onToggle={(name) => setSelectedHobbies((current) => current.includes(name)
            ? current.filter((item) => item !== name) : [...current, name])}
          onSaveAnswers={saveAnswers} onSaveHobbies={saveHobbies}
          onBack={() => setScreen("dashboard")} onSignOut={signOut}
          startAtPicker={Boolean(user.answers)} />
      )}
      {screen === "dashboard" && user && (
        <DashboardPage user={user} sessionId={sessionId}
          onOpenHobby={(name) => { setSelectedHobby(name); setScreen("roadmap"); }}
          onAddHobbies={beginOnboarding} onSignOut={signOut} />
      )}
      {screen === "roadmap" && user && (
        <HobbyProgressPage key={selectedHobby} user={user} sessionId={sessionId}
          hobbyName={selectedHobby} onBack={() => setScreen("dashboard")}
          onSaveSkill={saveSkillLevel} onProgressSaved={updateProgress} />
      )}
      <footer className="site-footer"><strong>HobBob</strong><span>Make a little room for what you love.</span><small>DEMO EXPERIENCE</small></footer>
    </div>
  );
}
