from fastapi import FastAPI
from app.auth.router import router as auth_router

app = FastAPI(title="FastAPI Auth System")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"msg": "Auth API running 🔥"}
