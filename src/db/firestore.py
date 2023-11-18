import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("/home/serb/HERMESHACKATHON/MyCFT-backend/mycft-c681e-firebase-adminsdk-5ekv3-f78850f623.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

users_collection = db.collection("Users").document("Frone")
users_collection.set({"Name" : "Frone", "email" : "frone@gmail.com"})