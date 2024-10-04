import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from daily_grid_generation import daily_grid, update_daily_grid

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

@app.get("/cron/dailyData/generate")
def generate_daily_data(request: Request) -> JSONResponse:
    authorization_header = request.headers.get("authorization")

    if not authorization_header:
        return JSONResponse({"error": "Missing authorization header"}, status_code=401)

    if authorization_header != f"Bearer {os.getenv('CRON_SECRET')}":
        return JSONResponse({"error": "Invalid authorization header"}, status_code=403)

    # Vercel discourages writing to files
    # Until a database is used, we don't save new puzzles to daily_grid.json
    update_daily_grid(save_to_file=False)

    return JSONResponse({"result": "success"})
