<script lang="ts" setup>
import { pokemonNames, searchIndex, validPokemon } from '../utils/userState';

defineProps<{
    name: string
    spriteUrl: string
}>()

function handleIsValidGuess(pokemonName: string) {
    if (validPokemon[searchIndex.value].includes(pokemonName)) {
        pokemonNames[searchIndex.value] = pokemonName
        console.log("CORRECT")
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
        <p class="grow text-left pl-2 capitalize">{{ name }}</p>
        <button class="btn bg-red-400" @click="handleIsValidGuess(name)">Guess</button>
    </div>
</template>
