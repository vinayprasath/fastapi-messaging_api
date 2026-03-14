from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
app=FastAPI()
client = MongoClient("mongodb://localhost:27017")
db = client["messaging_db"]
collection = db["messages"]

class Message(BaseModel):
    sender: str
    receiver: str
    text: str
@app.get("/")
def home():
    return{"message":"Messaging API running"}
@app.post("/send_message")
def send_message(msg: Message):
    message_dict=msg.dict()
    collection.insert_one(message_dict)

    
    return{"status":"Message stored in MongoDB"}
@app.get("/messages")
def get_messages():
    messages=list(collection.find({},{"_id":0}))
    return messages