# FastAPI Messaging API

This project is a simple REST API built using FastAPI and MongoDB.

## Features
- Send messages using POST API
- Retrieve stored messages using GET API
- Data validation using Pydantic
- MongoDB used as the database

## Technologies Used
- Python
- FastAPI
- MongoDB
- PyMongo

## API Endpoints

POST /send_message  
Send a message to the server.

GET /messages  
Retrieve all stored messages.

## How to Run

1. Install dependencies  
pip install fastapi uvicorn pymongo

2. Start the server  
uvicorn main:app --reload

3. Open browser  
http://127.0.0.1:8000/docs
