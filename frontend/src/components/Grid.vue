<script lang="ts" setup>
import Tile from './Tile.vue'

import Search from './Search.vue';
let pokemonNames = [
    "chimchar",
    "empoleon",
    "snorlax-gmax",
    "charmEleon",
    "scatterbug",
    "wurmple",
    "leavanny",
    "torkoal",
    "caterpie"
]



</script>

<template>
    <Search />
    <div class="overflow-hidden grid grid-cols-3 border border-black rounded-2xl">
        <Tile v-for="(name, index) in pokemonNames" :index="index" :name="name" />
    </div>
    
</template>

