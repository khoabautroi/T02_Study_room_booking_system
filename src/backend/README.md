# StudySpace Backend Skeleton

This is a minimal FastAPI skeleton. `main.py` contains the temporary runtime and health endpoint; no feature, database, authentication, or business code exists yet.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Verify the runtime at `http://127.0.0.1:8000/api/v1/health`.

## Structure

```text
main.py
features/
├── auth/       # includes profile
├── rooms/      # includes availability
├── bookings/   # includes cancellation and notifications
└── admin/
```

The feature owner adds routers, schemas, services, repositories, and tests only when implementation starts. Requirements are documented in `../../SYSTEM_BLUEPRINT.md`.
