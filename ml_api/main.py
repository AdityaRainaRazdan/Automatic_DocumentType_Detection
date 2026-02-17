from fastapi import FastAPI, UploadFile, File
import shutil
import os
from model import classify_document

app = FastAPI()

@app.post("/classify/")
async def classify(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = classify_document(temp_path)

    os.remove(temp_path)

    return result
