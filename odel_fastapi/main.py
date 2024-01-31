from pydoc import classname
import uuid
import cv2
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from random import randint
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, model_serializer
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.responses import RedirectResponse
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import asyncio
import sys
import os


app = FastAPI()

TEXTDIR = "texts/"

@app.post("/uploadstring/")
async def upload_string(content: str = Form(...)):
    try:
        # Generate a UUID as the filename
        file_name = str(uuid.uuid4()) + ".txt"
        file_path = f"texts/{file_name}"

        # Save the content to a text file
        with open(file_path, "w") as f:
            f.write(content)

        return JSONResponse(content={"message": f"String uploaded and saved as {file_name} successfully"}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {str(e)}"}, status_code=500)

