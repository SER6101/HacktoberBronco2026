# HacktoberBronco2026

HobBob hobby learning app.

## Run the app locally

Start the backend in one terminal:

```sh
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Then start the frontend in a second terminal:

```sh
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite. Demo accounts are stored in browser storage. The questionnaire is bundled with the frontend, and recommendations and hobby data are loaded from the backend through Vite's `/api` proxy.

## Frontend structure

- `frontend/src/pages/` contains the four screens: `AuthPage`, `HobbyPickerPage` (including the questionnaire), `DashboardPage`, and `HobbyProgressPage`.
- `frontend/src/App.jsx` coordinates screen navigation and shared user state.
- `frontend/src/services/demoUserStore.js` is the current browser-storage adapter. Replace this adapter with API calls when connecting backend accounts and progress.
- `frontend/src/data/hobbies.js` contains the questionnaire and optional visual metadata for hobby cards.
- `frontend/src/components/` contains shared UI components.

Build the frontend with `cd frontend && npm run build`.
