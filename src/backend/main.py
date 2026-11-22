"""Minimal FastAPI entry point for local development."""

import uvicorn
from fastapi import FastAPI


app = FastAPI(title="StudySpace API", version="0.1.0")


@app.get("/api/v1/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
