# HacktoberBronco2026

HobBob hobby learning app.

## Run the frontend demo

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite. The React demo uses browser storage and sample hobby content; authentication and progress are not yet connected to the backend.

## Frontend structure

- `frontend/src/pages/` contains the four screens: `AuthPage`, `HobbyPickerPage` (including the questionnaire), `DashboardPage`, and `HobbyProgressPage`.
- `frontend/src/App.jsx` coordinates screen navigation and shared user state.
- `frontend/src/services/demoUserStore.js` is the current browser-storage adapter. Replace this adapter with API calls when connecting backend accounts and progress.
- `frontend/src/data/hobbies.js` contains sample questionnaire, hobby, and roadmap content.
- `frontend/src/components/` contains shared UI components.

Build the frontend with `cd frontend && npm run build`.
