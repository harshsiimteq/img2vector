from .utils import extract_text_features, extract_image_features
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel
import requests
from io import BytesIO

app = FastAPI()

@app.post("/vector/text")
def vector_from_text(text: str = Form(...)):
    print(f"Received text: {text}")
    try:
        vector = extract_text_features(text)

        if hasattr(vector, 'tolist'):
            vector = vector.tolist()

        return {
            "status": "success",
            "data": {
                "vector": vector
            }
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "error",
            "error": str(e)
        })

class ImageURLRequest(BaseModel):
    image_url: str

@app.post("/vector/image")
async def vector_from_image_url(payload: ImageURLRequest):
    try:
        response = requests.get(payload.image_url)
        response.raise_for_status()

        image_file = BytesIO(response.content)
        vector = extract_image_features(image_file)

        if hasattr(vector, 'tolist'):
            vector = vector.tolist()

        return {
            "status": "success",
            "data": {
                "vector": vector
            }
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "error",
            "error": str(e)
        })
