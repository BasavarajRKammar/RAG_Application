from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import get_question, get_response
import uuid
class Message(BaseModel):
    msg: str
router = APIRouter()

@router.post('/')
def chat(request: Message):
    get_question(request.msg)
@router.get('/')
def get_responses():
    response = get_response()
    return response

@router.post('/create_sessionId')
def create_sessionId():
    session_id = str(uuid.uuid4())
    return {'session_id': session_id}

