from fastapi import APIRouter, UploadFile, File, HTTPException 
import pdfplumber

router = APIRouter(prefix = "/resume", tags=["Resume"])

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code = 400, detail= "Please update pdf file")

    try:
        text = ""
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        if not text.strip():
            raise HTTPException(status_code = 400, detail = "Coudn't Extract the text from the uploaded pdf")
        
        return{
            "filename" : file.filename,
            "text_preview" : text[:1000]
        }
    
    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))
         

