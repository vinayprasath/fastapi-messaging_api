from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Messaging API running"}

app.include_router(router)