from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.face_analysis import analyze_face_emotion

router = APIRouter()

@router.post("/emotion/face")
async def get_face_emotion(file: UploadFile = File(...)):
    try:
        # Read the uploaded image as bytes
        img_bytes = await file.read()

        # Analyze emotion from the face in the image
        results = analyze_face_emotion(img_bytes)

        # Return emotion analysis result
        return JSONResponse(content={"emotions": results})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
