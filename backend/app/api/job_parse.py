from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.job_parser import extract_structured_job

router = APIRouter(prefix="/job", tags=["Job Parsing"])


class JobParseRequest(BaseModel):
    text: str

@router.post("/parse")
def parse_resume(payload: JobParseRequest):
    try:
        structured_job = extract_structured_job(payload.text)
        return {
            "status": "success",
            "data": structured_job
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
