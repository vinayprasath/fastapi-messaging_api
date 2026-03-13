from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
messages =[]
class Message(BaseModel):
    sender: str
    receiver: str
    text: str
@app.get("/")
def home():
    return{"message":"Messaging API running"}
@app.post("/send_message")
def send_message(msg: Message):
    messages.append(msg)
    return{"status":"Message stored"}
@app.get("/messages")
def get_messages():
    return messages