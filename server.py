from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import uuid
import subprocess

app = FastAPI()

# middleware
app.add_middleware(
    CORSMiddleware, 
    allow_credentials=True, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)
output_dir = "./video"
@app.post("/uploadImage/")
async def upload_image(image: UploadFile = File(...), number: int = Form(...)):
    # Generate a unique filename using UUID
   
    
    return_video = os.path.join(output_dir, "test.mp4")
    return FileResponse(return_video, media_type="video/mp4")