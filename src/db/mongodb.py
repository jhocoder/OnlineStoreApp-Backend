from pymongo import MongoClient

def getDB():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tiendaonline"]
    return db
    
    