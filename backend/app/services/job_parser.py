import os
import json
from typing import List, Optional, Dict
from pydantic import BaseModel, ValidationError
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("BYTEZ_API_KEY"),
    base_url="https://api.bytez.com/models/v2/openai/v1"
)

class JobStructured(BaseModel):
    role: Optional[str]
    experience_level: Optional[str]

    required_skills: List[str]
    preferred_skills: List[str]

    responsibilities: List[str]
    nice_to_have: List[str]


def extract_structured_job(job_text: str) -> Dict:
    if not os.getenv("BYTEZ_API_KEY"):
        raise RuntimeError("BYTEZ_API_KEY not set")

    prompt = f"""
You are an expert job description parser.

Extract structured information from the job description below.

The job description may be written in long paragraphs without bullet points.

Rules:
- Return ONLY valid JSON
- Do NOT include explanations
- Use null if information is missing
- Normalize skill names (e.g. React-Native → React Native)

Output format:
{{
  "role": null,
  "experience_level": null,
  "required_skills": [],
  "preferred_skills": [],
  "responsibilities": [],
  "nice_to_have": []
}}

Job Description:
\"\"\"
{job_text}
\"\"\"
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2-7B-Instruct",  
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=900
    )

    try:
        raw_json = response.choices[0].message.content
        parsed = json.loads(raw_json)
        validated = JobStructured(**parsed)
        return validated.model_dump()

    except json.JSONDecodeError:
        raise ValueError("LLM did not return valid JSON")

    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {e}")
