from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from firebase_config import db

router = APIRouter()

# Pydantic model for user input
class User(BaseModel):
    name: str
    email: str
    # Add additional fields as needed

@router.get("/get_document/{collection}/{doc_id}")
async def get_document(collection: str, doc_id: str):
    try:
        doc_ref = db.collection(collection).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving document: {str(e)}")

@router.get("/users")
def get_users():
    try:
        users_ref = db.collection('users')
        docs = users_ref.stream()
        users = [doc.to_dict() for doc in docs]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving users: {str(e)}")

@router.post("/add_document/{collection}")
async def add_document(collection: str, data: dict = Body(...)):
    try:
        doc_ref = db.collection(collection).add(data)
        return {"message": "Document added successfully", "document_id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding document: {str(e)}")

@router.post("/add_user")
def add_user(user: User):
    try:
        user_ref = db.collection('users').add(user.dict())
        return {"status": "success", "message": "User added", "user_id": user_ref.id}
    except Exception as e:
        return {"status": "failure", "message": f"Error adding user: {str(e)}"}
