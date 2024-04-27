import random, copy, json, schedule, time, threading

category_data: dict = json.load(open("category_data.json", "r"))

for key, value in category_data.items():
    category_data[key] = set(value)

categories = list(category_data.keys())

def generate_categories(unused_categories: list):
    selected_categories = []
    for _ in range(3):
        selected_categories.append(unused_categories.pop(random.randrange(len(unused_categories))))
    return selected_categories

def get_results(categories: list):
    return [
        category_data[category]
        for category in categories
    ]

def generate_new_grid():
    retries = 0
    
    while True:
        unused_categories = copy.deepcopy(categories)
        
        column_categories = generate_categories(unused_categories)
        column_results = get_results(column_categories)
        
        row_categories = generate_categories(unused_categories)
        row_results = get_results(row_categories)
        
        valid_pokemon = [
            # Finds the intersection between the two sets
            list(column_result & row_result)
            for row_result in row_results
            for column_result in column_results
        ]
        
        # Returns generated data if no cells contains no valid pokemon
        if not any(len(sublist) == 0 for sublist in valid_pokemon):
            return {
                "validPokemon": valid_pokemon,
                "columnCategories": column_categories,
                "rowCategories": row_categories
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
schedule.every().day.do(update_daily_grid)

def check_for_scheduled_tasks():
    while True:
        print("Checking for scheduled events...")
        schedule.run_pending()
        time.sleep(100)

scheduled_thread = threading.Thread(target=check_for_scheduled_tasks)
scheduled_thread.daemon = True
scheduled_thread.start()