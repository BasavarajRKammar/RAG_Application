from fastapi import APIRouter, UploadFile,File
from app.services.embeding import get_document
router = APIRouter()

@router.post('/')
async def upload_file(file: UploadFile =File(...)):
   file_path = f'filetemp_{file.filename}'
   with open(file_path,'wb') as f:
      f.write(await file.read())
   get_document(file_path)
   return {
        'filename': file.filename,
    }
    