from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.pipeline import process_video
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://elaborate-begonia-4b49b4.netlify.app"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Real-Time Summarization API Running"
    }


@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):

    print("UPLOAD REQUEST RECEIVED")

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    print("Saving file...")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    print("Starting pipeline...")

    result = process_video(file_path)

    print("Pipeline completed")

    return result
