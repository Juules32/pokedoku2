import httpx, random, copy, json, schedule, time, threading

all_pokemon_response = httpx.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
all_pokemon_text = all_pokemon_response.text

pokemon_types = [
    "bug",
    "dark",
    "dragon",
    "electric",
    "fairy",
    "fighting",
    "fire",
    "flying",
    "ghost",
    "grass",
    "ground",
    "ice",
    "normal",
    "poison",
    "psychic",
    "rock",
    "steel",
    "water"
]

categories = [
    "type"
]

def get_pokemon_of_type(type) -> set:
    response = httpx.get(f'https://pokeapi.co/api/v2/type/{type}').json()["pokemon"]
    return {entry['pokemon']['name'] for entry in response}

def generate_new_grid():
    retries = 0
    
    while True:
        unused_types = copy.deepcopy(pokemon_types)
        
        column_categories = [
            random.choice(categories)
            for _ in range(3)
        ]
        
        row_categories = [
            random.choice(categories)
            for _ in range(3)
        ]
        
        column_contents = []
        for category in column_categories:
            if category == "type":
                column_contents.append(unused_types.pop(random.randrange(len(unused_types))))
            # Add handling of other content here
        
        row_contents = []
        for category in row_categories:
            if category == "type":
                row_contents.append(unused_types.pop(random.randrange(len(unused_types))))
            # Add handling of other content here
        
        column_criteria = [
            {
                "category": column_categories[i],
                "content": column_contents[i]
            }
            for i in range(3)
        ]
        row_criteria = [
            {
                "category": row_categories[i],
                "content": row_contents[i]
            }
            for i in range(3)
        ]
        
        column_results = [
            get_pokemon_of_type(entry["content"])
            for entry in column_criteria
        ]
        
        row_results = [
            get_pokemon_of_type(entry["content"])
            for entry in row_criteria
        ]
        
        valid_pokemon = [
            list(column_result & row_result)
            for row_result in row_results
            for column_result in column_results
        ]
        
        # Returns generated data if no cells contains no valid pokemon
        if not any(len(sublist) == 0 for sublist in valid_pokemon):
            return {
                "validPokemon": valid_pokemon,
                "columnCriteria": column_criteria,
                "rowCriteria": row_criteria
            }
        else:
            retries += 1
            print(f"Combination of categories contained empty result. Retries: ${retries}")

def load_daily_grid_json():
    with open("daily_grid.json", "r") as daily_grid_json:
        loaded_json = json.load(daily_grid_json)
    print("Loaded daily grid data!")
    return loaded_json

daily_grid = load_daily_grid_json()
# daily_grid = generate_new_grid() # for development

def update_daily_grid():
    global daily_grid

    new_grid = generate_new_grid()
    with open("daily_grid.json", "w") as daily_grid_json:
        json.dump(new_grid, daily_grid_json, indent=4)
        
    daily_grid.update(new_grid)
    print("Updated daily grid data!")

# Schedules the grid data to update every new day
schedule.every().day.at("00:00").do(update_daily_grid)

def check_for_scheduled_tasks():
    while True:
        print("Checking for scheduled events...")
        schedule.run_pending()
        time.sleep(1000)

scheduled_thread = threading.Thread(target=check_for_scheduled_tasks)
scheduled_thread.daemon = True
scheduled_thread.start()