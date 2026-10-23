// Vite proxy handles /api locally. For a deployed frontend set VITE_API_URL.
const BASE = (import.meta.env.VITE_API_URL || "/api").replace(/\/$/, "");

async function request(path, options = {}) {
  const response = await fetch(`${BASE}${path}`, {
    ...options,
    headers: { "Content-Type": "application/json", ...options.headers },
  });
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(typeof body.detail === "string" ? body.detail : `API error ${response.status}`);
  }
  return response.json();
}
const hobbyPath = (name) => `/hobby/${encodeURIComponent(name)}`;
const params = (values) => new URLSearchParams(values).toString();

export const getQuestions = () => request("/questions");
export const getHobbies = () => request("/hobbies");
export const submitQuestionnaire = (answers) => request("/recommend", {
  method: "POST", body: JSON.stringify({ answers }),
});
export const getHobbyInfo = (name) => request(hobbyPath(name));
export const selectSkill = (name, skill, sessionId) => request(`${hobbyPath(name)}/select-skill`, {
  method: "POST", body: JSON.stringify({ skill, session_id: sessionId }),
});
export const getProgress = (name, skill, sessionId) => request(
  `${hobbyPath(name)}/progress/${encodeURIComponent(skill)}?${params({ session_id: sessionId })}`
);
export const getLesson = (name, number, skill, sessionId) => request(
  `${hobbyPath(name)}/lesson/${number}?${params({ skill, session_id: sessionId })}`
);
export const completeLesson = (name, sessionId, skill, number, readingFinished, videoFinished) => request(
  `${hobbyPath(name)}/complete-lesson`, {
    method: "POST",
    body: JSON.stringify({ session_id: sessionId, skill, lesson_number: number,
      reading_finished: readingFinished, video_finished: videoFinished }),
  }
);
export const getAchievements = (name, sessionId, skill, completedQuests = []) => request(
  `${hobbyPath(name)}/achievements`, {
    method: "POST", body: JSON.stringify({ session_id: sessionId, skill, completed_quests: completedQuests }),
  }
);
