# 🚀 DevOps Platform Lab

A production-oriented DevOps laboratory demonstrating how to build, secure, containerize, deploy and monitor a cloud-native application.

This repository starts with a small FastAPI service and a working CI foundation. The next stages are container publishing, Helm deployment, GitOps, and observability.

## What is in place

- REST API with a welcome endpoint and a health check
- Automated endpoint tests with pytest
- GitHub Actions workflow that runs the tests on pushes and pull requests
- Dockerfile for running the API as a container

## Run locally

Requires Python 3.12 or newer.

```bash
python -m venv .venv
# Activate the environment:
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API docs, or call the health check:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Run the tests:

```bash
python -m pytest -q
```

## Run with Docker

```bash
docker build -t devops-platform-lab .
docker run --rm -p 8000:8000 devops-platform-lab
```

Then visit [http://localhost:8000/health](http://localhost:8000/health).

## Architecture

```text
Developer -> GitHub -> GitHub Actions (tests) -> Docker image -> Kubernetes/Helm
                                                        └----> monitoring (planned)
```

The current implementation covers the API, tests, and CI foundation. Container publishing, Kubernetes/Helm deployment, GitOps, and monitoring are planned follow-up stages.
