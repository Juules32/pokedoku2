import axios from "axios";
import { Pokemon } from "./interfaces";

function customSort(a: Pokemon, b: Pokemon, searchLowerCase: string): number {
    // Check if names start with the search string
    const startsWithSearchStringA = a.name.toLowerCase().startsWith(searchLowerCase);
    const startsWithSearchStringB = b.name.toLowerCase().startsWith(searchLowerCase);

    // Sort names starting with the search string first
    if (startsWithSearchStringA && !startsWithSearchStringB) {
        return -1;
    } else if (!startsWithSearchStringA && startsWithSearchStringB) {
        return 1;
    } else {
        // For other cases, sort alphabetically
        return a.name.localeCompare(b.name);
    }
}

export async function getSearchData(search: string) {
    try {
        const response = await axios.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0");
        if (!response.data) {
            throw new Error('Response data not found');
        }
        const searchLowerCase = search.toLowerCase()
        const filteredResponse =
            response.data.results.filter((pokemon: Pokemon) => pokemon.name.toLowerCase().includes(searchLowerCase))
            .sort((a: Pokemon, b: Pokemon) => customSort(a, b, searchLowerCase))
            .slice(0, 10)

        const spriteUrls = await Promise.all(filteredResponse.map(async (pokemon: Pokemon) => {
            const spriteUrl = await getPokemonSprite(pokemon.url);
            return { name: pokemon.name, spriteUrl };
        }));
        return spriteUrls
    } catch (error) {

    }
}

export async function getPokemonSprite(url: string) {
    try {
        const response = await axios.get(url);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        return response.data.sprites.front_default
    } catch (error) {

    }
}