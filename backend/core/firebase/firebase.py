import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import APIRouter
import os

# ✅ Correct relative path to JSON key
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CRED_PATH = os.path.join(BASE_DIR, "serenity-dbd18-firebase-adminsdk-fbsvc-e4f0e1a671.json")

# ✅ Initialize Firebase first
cred = credentials.Certificate(CRED_PATH)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# ✅ Setup Firestore client
db = firestore.client()

# ✅ FastAPI router setup
router = APIRouter()

@router.get("/users")
def get_users():
    users_ref = db.collection('users')
    docs = users_ref.stream()
    users = [doc.to_dict() for doc in docs]
    return users

@router.post("/add_user")
def add_user(user: dict):
    db.collection('users').add(user)
    return {"status": "success", "message": "User added"}
