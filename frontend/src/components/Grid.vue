<script lang="ts" setup>
import Tile from './Tile.vue'
import Search from './Search.vue';
import { pokemonNames, searchIndex } from '../utils/userState';

function handleShowSearch(index: number) {
    searchIndex.value = index
    console.log(`Currently searching for tile with index ${index}`)
}

function handleCloseSearch(event: Event) {
	if ((event.target as HTMLElement).id == 'background') {
        searchIndex.value = -1
    }
}
</script>

<template>
    <div class="overflow-hidden grid grid-cols-3 border border-black rounded-2xl">
        <Tile 
            v-for="(name, index) in pokemonNames" 
            :index="index" 
            :key="name" 
            :name="name" 
            @click="handleShowSearch(index)"
        />
    </div>
    <Search v-if="searchIndex >= 0" @click="handleCloseSearch" />

</template>
