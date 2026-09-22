"""Small REST API used by the DevOps Platform Lab."""

from fastapi import FastAPI

app = FastAPI(
    title="DevOps Platform Lab API",
    description="A small API for demonstrating a production-oriented DevOps workflow.",
    version="0.1.0",
)


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    """Return a short welcome message."""
    return {"message": "DevOps Platform Lab API", "docs": "/docs"}


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Report whether the API process is responding."""
    return {"status": "ok"}
