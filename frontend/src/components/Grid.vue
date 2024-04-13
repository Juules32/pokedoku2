<script lang="ts" setup>
import Tile from './Tile.vue'
import Search from './Search.vue';
import { pokemonNames, searchIndex, columnCriteria, rowCriteria } from '../utils/userState';
import Criteria from './Criteria.vue';

function handleShowSearch(index: number) {
    searchIndex.value = index
    console.log(`Currently searching for tile with index ${index}`)
}

function handleCloseSearch(event: Event) {
	if ((event.target as HTMLElement).id == 'background') {
        searchIndex.value = -1
    }
}

function gridIndexToPokeIndex(index: number) {
    const validIndeces = [6, 7, 8, 11, 12, 13, 16, 17, 18]
    return validIndeces.indexOf(index)
}

function gridIndexToCriteriaIndex(index: number) {
    const validRowOrColumnIndeces = [1, 2, 3, 5, 10, 15]
    return validRowOrColumnIndeces.indexOf(index)
}

function getCriteriaName(index: number) {
    const criteriaIndex = gridIndexToCriteriaIndex(index)
    if (criteriaIndex >= 3) {
        return rowCriteria[criteriaIndex % 3]
    }
    else {
        return columnCriteria[criteriaIndex]
    }
}

</script>

<template>
    <div>

        <div class="size-fit overflow-hidden grid grid-cols-5">
            <div v-for="index in [...Array(25).keys()]">
                <Tile 
                    v-if="gridIndexToPokeIndex(index) >= 0"
                    :index="gridIndexToPokeIndex(index)"
                    :key="pokemonNames[gridIndexToPokeIndex(index)]" 
                    :name="pokemonNames[gridIndexToPokeIndex(index)]" 
                    @click="handleShowSearch(gridIndexToPokeIndex(index))"
                />
                <Criteria 
                    v-else-if="gridIndexToCriteriaIndex(index) >= 0" 
                    :criteriaName="getCriteriaName(index)"
                />
                <div v-else></div>
            </div>
        </div>
    </div>
    <Search v-if="searchIndex >= 0" @click="handleCloseSearch" />

</template>
