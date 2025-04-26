from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_journal():
    return {"message": "Journal endpoint working"}
