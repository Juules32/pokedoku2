import random, copy, json

criteria_data: dict = json.load(open("criteria_data.json", "r"))

for key, value in criteria_data.items():
    criteria_data[key] = set(value)

criteria = list(criteria_data.keys())

def generate_criteria(unused_criteria: list):
    selected_criteria = []
    for _ in range(3):
        selected_criteria.append(unused_criteria.pop(random.randrange(len(unused_criteria))))
    return selected_criteria

def get_results(criteria: list):
    return [
        criteria_data[criterion]
        for criterion in criteria
    ]

def generate_new_grid():
    retries = 0
    
    while True:
        unused_criteria = copy.deepcopy(criteria)
        
        column_criteria = generate_criteria(unused_criteria)
        column_results = get_results(column_criteria)
        
        row_criteria = generate_criteria(unused_criteria)
        row_results = get_results(row_criteria)
        
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
                "columnCriteria": column_criteria,
                "rowCriteria": row_criteria
            }
        else:
            retries += 1
            print(f"Combination of criteria contained empty result. Retries: ${retries}")

def load_daily_grid_json():
    with open("daily_grid.json", "r") as daily_grid_json:
        loaded_json = json.load(daily_grid_json)
    print("Loaded daily grid data!")
    return loaded_json

def update_daily_grid(save_to_file: bool = True):
    global daily_grid

    new_grid = generate_new_grid()

    if save_to_file:
        with open("daily_grid.json", "w") as daily_grid_json:
            json.dump(new_grid, daily_grid_json, indent=4)
        
    daily_grid.update(new_grid)
    print("Updated daily grid data!")

daily_grid = load_daily_grid_json()
