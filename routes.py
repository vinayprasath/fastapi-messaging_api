from fastapi import APIRouter
from models import Message
from database import collection

router = APIRouter()

@router.post("/send_message")
def send_message(msg: Message):
    message_dict = msg.dict()
    collection.insert_one(message_dict)
    return {"status": "Message stored in MongoDB"}


@router.get("/messages")
def get_messages():
    messages = list(collection.find({}, {"_id": 0}))
    return messages