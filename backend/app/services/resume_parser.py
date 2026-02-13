import os
import json
from typing import Dict, Optional, List
from pydantic import BaseModel, ValidationError
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("BYTEZ_API_KEY"),
    base_url="https://api.bytez.com/models/v2/openai/v1"
)

class ResumeStructured(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]

    skills: Dict
    experience: List
    projects: List
    education: List


def extract_structured_resume(resume_text: str) -> Dict:
    if not os.getenv("BYTEZ_API_KEY"):
        raise RuntimeError("BYTEZ_API_KEY not set")

    prompt = f"""
You are an expert resume parser.

Extract structured information from the resume text below.

Rules:
- Return ONLY valid JSON
- Do NOT include explanations
- Use null if missing

Output format:
{{
  "name": null,
  "email": null,
  "phone": null,
  "skills": {{
    "languages": [],
    "frameworks_tools": [],
    "other": []
  }},
  "experience": [],
  "projects": [],
  "education": []
}}

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2-7B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=800
    )

    try:
        raw_json = response.choices[0].message.content
        parsed = json.loads(raw_json)
        validated = ResumeStructured(**parsed)
        # return validated.dict()
        return validated.model_dump()

    except json.JSONDecodeError:
        raise ValueError("LLM did not return valid JSON")

    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {e}")
