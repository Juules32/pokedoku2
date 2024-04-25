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

pokemon_regions = [
    "kanto",
    "johto",
    "hoenn",
    "sinnoh",
    "unova",
    "kalos",
    "alola",
    "galar",
    "paldea"
]

region_to_generation = { k:v for (k,v) in zip(pokemon_regions, range(1, 10))}  

categories = [
    "type",
    "region"
]

def get_pokemon_of_type(type) -> set:
    response = httpx.get(f'https://pokeapi.co/api/v2/type/{type}').json()["pokemon"]
    return {entry['pokemon']['name'] for entry in response}

def get_pokemon_from_region(region) -> set:
    generation = region_to_generation[region]
    response = httpx.get(f'https://pokeapi.co/api/v2/generation/{generation}').json()["pokemon_species"]
    return {entry['name'] for entry in response}

def get_query_type(category):
    if category == "type":
        return get_pokemon_of_type
    if category == "region":
        return get_pokemon_from_region


def generate_categories():
    return [
        random.choice(categories)
        for _ in range(3)
    ]

def generate_contents(categories, unused_types, unused_regions):
    contents = []
    for category in categories:
        if category == "type":
            contents.append(unused_types.pop(random.randrange(len(unused_types))))
        if category == "region":
            contents.append(unused_regions.pop(random.randrange(len(unused_regions))))
    return contents

def generate_criteria(categories, contents):
    return [
        {
            "category": categories[i],
            "content": contents[i]
        }
        for i in range(3)
    ]

def get_results(criteria):
    return [
        get_query_type(entry["category"])(entry["content"])
        for entry in criteria
    ]

def generate_new_grid():
    retries = 0
    
    while True:
        unused_types = copy.deepcopy(pokemon_types)
        unused_regions = copy.deepcopy(pokemon_regions)
        
        column_categories = generate_categories()
        column_contents = generate_contents(column_categories, unused_types, unused_regions)
        column_criteria = generate_criteria(column_categories, column_contents)
        column_results = get_results(column_criteria)
        
        row_categories = generate_categories()
        row_contents = generate_contents(row_categories, unused_types, unused_regions)
        row_criteria = generate_criteria(row_categories, row_contents)
        row_results = get_results(row_criteria)
        
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

def update_daily_grid():
    global daily_grid

    new_grid = generate_new_grid()
    with open("daily_grid.json", "w") as daily_grid_json:
        json.dump(new_grid, daily_grid_json, indent=4)
        
    daily_grid.update(new_grid)
    print("Updated daily grid data!")

daily_grid = load_daily_grid_json()
# update_daily_grid() # for development
# daily_grid = generate_new_grid() # for development

# Schedules the grid data to update every new day
schedule.every().day.at("00:00").do(update_daily_grid)

def check_for_scheduled_tasks():
    while True:
        print("Checking for scheduled events...")
        schedule.run_pending()
        time.sleep(100)

scheduled_thread = threading.Thread(target=check_for_scheduled_tasks)
scheduled_thread.daemon = True
scheduled_thread.start()