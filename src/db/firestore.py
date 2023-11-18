import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json


cred = credentials.Certificate("/home/serb/HERMESHACKATHON/MyCFT-backend/mycft-c681e-firebase-adminsdk-5ekv3-f78850f623.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def db_get_user(id: str):
    user = db.collection("Users").document(id)
    user_data = user.get()
    if user_data.exists:
        return json.dumps(user_data.to_dict())
    else:
        return "ERROR"
    

def db_set_user(id: str, user_data):
    user = db.collection("Users").document(id)
    print(user_data)
    user.set(user_data)

# users_collection = db.collection("Users").document("Frone")
# users_collection.set({"Name" : "Frone", "email" : "frone@gmail.com"})