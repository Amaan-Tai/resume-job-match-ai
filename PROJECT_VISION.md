# Resume -> Job Match AI Tool

## Problem Statement
Job seekers apply to roles without understanding how well their resume matches the job requirements, leading to repeated rejections and frustration.

## Solution Overview
This project is an AI-powered Resume–Job Matching system that analyzes a candidate’s resume against a job description and provides a job fit score, identifies missing skills, and suggests resume improvements using LLMs and Retrieval-Augmented Generation (RAG).

## Target Users
- Final-year students
- Freshers and early-career professionals
- Career switchers

## MVP Scope
- Upload resume (PDF)
- Input a single job description
- Extract resume and job requirements
- Generate job fit score (0–100%)
- Provide missing skills and improvement tips

## Out of Scope (For MVP)
- User authentication
- Multiple resumes comparison
- Payments or subscriptions
- Company-side dashboards

## Success Criteria
- Resume and job description are parsed accurately
- Job fit score feels realistic and explainable
- Suggestions are actionable and relevant

## Tech Stack (Initial)
- Backend: Python, FastAPI
- AI: LLMs, Embeddings, RAG
- Vector DB: ChromaDB
- Frontend: React
