from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["messaging_db"]

collection = db["messages"]