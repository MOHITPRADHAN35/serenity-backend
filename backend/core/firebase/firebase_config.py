import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serenity-dbd18-firebase-adminsdk-fbsvc-e4f0e1a671.json")

# Prevent re-initialization
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
