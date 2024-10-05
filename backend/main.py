import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from db_business import set_tomorrows_puzzle, get_puzzle_from_date
from date import get_date_str

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todaysPuzzle")
def get_todays_puzzle() -> JSONResponse:
    return JSONResponse(get_puzzle_from_date(get_date_str()), status_code=200)

@app.get("/puzzle/{date}")
def get_puzzle(date: str) -> JSONResponse:
    return JSONResponse(get_puzzle_from_date(date), status_code=200)

@app.get("/cron/generateTomorrowsPuzzle")
def generate_daily_data(request: Request) -> JSONResponse:
    authorization_header = request.headers.get("authorization")

    if not authorization_header:
        return JSONResponse({"error": "Missing authorization header"}, status_code=401)

    if authorization_header != f"Bearer {os.getenv('CRON_SECRET')}":
        return JSONResponse({"error": "Invalid authorization header"}, status_code=403)

    set_tomorrows_puzzle()

    return JSONResponse({"result": "success"}, status_code=200)
