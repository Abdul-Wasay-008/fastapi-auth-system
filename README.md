# 🔐 FastAPI Authentication System

A simple authentication system built with FastAPI. It contains:
- JWT authentication
- Password hashing
- Dependency-based authorization

## Features
- Signup
- Login
- Protected routes

## Tech Stack
- FastAPI
- Python
- JWT (python-jose)
- Passlib (bcrypt)

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs