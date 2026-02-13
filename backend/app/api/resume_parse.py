from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.resume_parser import extract_structured_resume

router = APIRouter(prefix="/resume", tags=["Resume Parsing"])


class ResumeParseRequest(BaseModel):
    text: str


@router.post("/parse")
def parse_resume(payload: ResumeParseRequest):
    try:
        structured_resume = extract_structured_resume(payload.text)
        return {
            "status": "success",
            "data": structured_resume
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
