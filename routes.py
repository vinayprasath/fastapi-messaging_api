from fastapi import APIRouter,HTTPException
from models import Message
from database import collection
from bson import ObjectId


router = APIRouter()

@router.post("/send_message")
def send_message(msg: Message):
    message_dict = msg.dict()
    collection.insert_one(message_dict)
    return {"status": "Message stored in MongoDB"}


@router.get("/messages")
def get_messages():
    messages = []

    for msg in collection.find():
        msg["_id"] = str(msg["_id"])
        messages.append(msg)

    return messages

#FOR DELETE MESSAGE API


@router.delete("/message/{id}")
def delete_message(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"status": "Message deleted"}

#for updates msg API
@router.put("/message/{id}")
def update_message(id: str, msg: Message):
    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": msg.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"status": "Message updated"}