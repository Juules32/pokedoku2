<script lang="ts" setup>
import { pokemonNames, searchIndex, validPokemon } from '../utils/userState';
import { capitalize } from '../utils/stringManip';

defineProps<{
    name: string
    spriteUrl: string
}>()

function handleIsValidGuess(pokemonName: string) {
    console.log(pokemonName, validPokemon)

    if (validPokemon[searchIndex.value].includes(pokemonName)) {
        pokemonNames[searchIndex.value] = pokemonName
    }
    else {
        console.log("WRONG")
    }
    // Add logic for determining if it was a valid guess    
    searchIndex.value = -1
}
</script>

<template>
    <div class="flex items-center p-2">

        <img :src="spriteUrl" />
        <p class="grow text-left pl-2">{{ capitalize(name) }}</p>
        <button class="btn bg-red-400" @click="handleIsValidGuess(name)">Guess</button>
    </div>
</template>
