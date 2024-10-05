import httpx, json
from collections import defaultdict

def is_name_legal(name):
    if (
        "zygarde-" in name or
        "rockruff-" in name or
        "cramorant-" in name or
        "greninja-" in name or
        "-totem" in name or
        ("pikachu-" in name and name != "pikachu-gmax") or
        ("eevee-" in name and name != "eevee-gmax")
    ):
        return False
    else:
        return True

generation_to_region = {
    "generation-i": "kanto",
    "generation-ii": "johto",
    "generation-iii": "hoenn",
    "generation-iv": "sinnoh",
    "generation-v": "unova",
    "generation-vi": "kalos",
    "generation-vii": "alola",
    "generation-viii": "galar",
    "generation-ix": "paldea"
}

def find_region(name, species_generation):
    
    # Exceptions where species belongs to different region
    # than the generation it was introduced in
    if name == "wyrdeer": return "hisui"
    if name == "kleavor": return "hisui"
    if name == "overqwil": return "hisui"
    if name == "ursaluna": return "hisui"
    if name == "basculegion": return "hisui"
    if name == "sneasler": return "hisui"
    if name == "enamorus": return "hisui"
    if "-hisui" in name: return "hisui"
    if "-paldea" in name: return "paldea"
    if "-galar" in name: return "galar"
    if "-alola" in name: return "alola"
    if name == "basculin-white-striped": return "hisui"
    if name == "ursaluna-bloodmoon": return "paldea"
    
    # If no exceptions, return the corresponding region
    return generation_to_region[species_generation]

criteria = defaultdict(lambda : [])

popular_moves = ["stomp", "fly", "bite"]

def add(criterion, name):
    criteria[criterion].append(name)

def add_predefined_criteria():
    criteria["fossil"] = [
        "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl", "aerodactyl-mega", "lileep", "cradily", "anorith", "armaldo", "cranidos", "rampardos", "shieldon", "bastiodon", "tirtouga", "carracosta", "archen", "archeops", "genesect", "tyrunt", "tyrantrum", "amaura", "aurorus", "dracozolt", "arctozolt", "dracovish", "arctovish"
    ]
    criteria["starter"] = [
        "bulbasaur", "charmander", "squirtle", "chikorita", "cyndaquil", "totodile", "treecko", "torchic", "mudkip", "turtwig", "chimchar", "piplup", "snivy", "tepig", "oshawott", "chespin", "fennekin", "froakie", "rowlet", "litten", "popplio", "grookey", "scorbunny", "sobble", "sprigatito", "fuecoco", "quaxly", "pikachu", "eevee"
    ]
    criteria["ultra-beast"] = [
        "nihilego", "buzzwole", "pheromosa", "xurkitree", "celesteela", "kartana", "guzzlord", "necrozma", "poipole", "naganadel", "stakataka", "blacephalon"
    ]
    criteria["paradox"] = [
        "great-tusk", "scream-tail", "brute-bonnet", "flutter-mane", "slither-wing", "sandy-shocks", "roaring-moon", "koraidon", "walking-wake", "raging-bolt", "gouging-fire", "iron-treads", "iron-bundle", "iron-hands", "iron-jugulis", "iron-moth", "iron-thorns", "iron-valiant", "miraidon", "iron-leaves", "iron-crown", "iron-boulder"
    ]
    
add_predefined_criteria()

limit = 10000
offset = 0

def save_criteria_data_to_json():
    results = httpx.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}').json()["results"]
    for result in results:
        name = result["name"]
        
        # Ignores specific pokemon
        if not is_name_legal(name): continue
        
        pokemon_data = httpx.get(result['url']).json()
        pokedex_number = pokemon_data["id"]
        print(f"Generating data for: {name} (no. {pokedex_number})")
        
        # Types
        types = pokemon_data["types"]
        if len(types) == 1:
            add("mono-type", name)
        if len(types) == 2:
            add("dual-type", name)
        for type_data in types:
            pokemon_type = type_data["type"]["name"]
            add(f"type-{pokemon_type}", name)
        
        # Special types of pokemon
        if "-mega" in name:
            add("mega", name)
        if "-gmax" in name:
            add("gmax", name)
        
        # Moves
        move_names = [entry["move"]["name"] for entry in pokemon_data["moves"]]
        for popular_move in popular_moves:
            if popular_move in move_names:
                add(f"knows-{popular_move}", name)
        
        # Pokemon-species
        species_url = pokemon_data["species"]["url"]
        species_data = httpx.get(species_url).json()
        
        # Special types of pokemon
        if species_data["is_baby"]:
            add("baby", name)
        if species_data["is_legendary"]:
            add("legendary", name)
        if species_data["is_mythical"]:
            add("mythical", name)
        
        # Region
        species_generation = species_data["generation"]["name"]
        add(f'region-{find_region(name, species_generation)}', name)
        
    # Dumps criteria into one big json file
    with open("criteria_data.json", "w") as criteria_data_json:
        json.dump(criteria, criteria_data_json, indent=4)
    print("Queried and stored all criteria information")

# Running this script generates and saves all criteria (takes a while)
if __name__ == "__main__":
    save_criteria_data_to_json()
