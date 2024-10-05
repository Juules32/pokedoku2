from daily_grid_generation import generate_new_grid
from db import db
import json
from date import get_date_str

def set_new_puzzle(date: str, save_to_db: bool = False, save_to_file: bool = False) -> None:
    new_grid = generate_new_grid()

    if save_to_db:
        db.set_puzzle(date, new_grid)
        print("Updated daily grid data!")

    elif save_to_file:
        with open("daily_grid.json", "w") as daily_grid_json:
            json.dump(new_grid, daily_grid_json, indent=4)
            print("Updated daily grid data!")

def set_tomorrows_puzzle() -> None:
    set_new_puzzle(get_date_str(1), save_to_db=True)

def get_puzzle_from_date(date: str) -> dict:
    return db.get_puzzle(date)

# Running this script generates and saves a new daily grid to file
if __name__ == "__main__":
    set_new_puzzle(date=get_date_str(), save_to_db=True)
