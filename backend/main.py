import os
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from daily_grid_generation import daily_grid
load_dotenv()

FRONTEND_HOST = os.getenv("FRONTEND_HOST")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{FRONTEND_HOST}", f"https://{FRONTEND_HOST}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/answer")
def get_answer():
    return {"answer": 42}

@app.get("/dailyData")
def get_daily_data():
    return daily_grid
