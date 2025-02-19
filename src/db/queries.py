from db.mongodb import getDB
from bson import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash


db = getDB()
user_collections = db["usuarios"]
products_collections = db["productos"]



def register(email, username, password):
    searchUser = user_collections.find_one({"email": email})
    
    if searchUser:
        return False
    
    return user_collections.insert_one({'email': email, 'username':username, 'password':password})

def login(email, password):
    searchUser = user_collections.find_one({"email": email})
    
    if searchUser and check_password_hash(searchUser["password"], password):
        return searchUser
    else:
        return False
    
    
def addProduct(nombre, descripcion, precio, categoria, stock):
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "categoria": categoria,
        "stock": stock
       }
    add = products_collections.insert_one(producto)
    if add:
        return add

def getProducts():
    return list(products_collections.find())

def getProduct(id):
    return products_collections.find_one({"_id":ObjectId(id)})

def updateProduct(id,nombre, descripcion, precio, categoria, stock):
    return products_collections.update_one({"_id": ObjectId(id)}, {"$set":{
        "nombre":nombre,
        "descripcion": descripcion,
        "precio":precio,
        "categoria": categoria,
        "stock": stock
    }})
    
def deleteProduct(id):
    return products_collections.delete_one({"_id" : ObjectId(id)})

def descProducts():
    return products_collections.find().sort({"precio": -1})

def ascProducts():
    return products_collections.find().sort({"precio": 1})