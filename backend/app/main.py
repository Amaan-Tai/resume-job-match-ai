from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.resume import router as resume_router
from app.api.resume_parse import router as resume_parse_router

app = FastAPI(
    title="Resume Job Match AI",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(resume_router)
app.include_router(resume_parse_router)

@app.get("/")
def root():
    return {"message": "Resume Job Match AI backend is running"}
