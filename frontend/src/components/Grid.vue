<script lang="ts" setup>
import Tile from './Tile.vue'
import Search from './Search.vue';
import { pokemonNames, searchIndex, columnCriteria, rowCriteria } from '../utils/userState';
import Criterion from './Criterion.vue';
import { useWindowSize } from 'vue-window-size';

function handleShowSearch(index: number) {
    searchIndex.value = index
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

function gridIndexToCriterionIndex(index: number) {
    const validRowOrColumnIndeces = [1, 2, 3, 5, 10, 15]
    return validRowOrColumnIndeces.indexOf(index)
}

function getCriterion(index: number) {
    const criterionIndex = gridIndexToCriterionIndex(index)
    if (criterionIndex >= 3) {
        return rowCriteria[criterionIndex % 3]
    }
    else {
        return columnCriteria[criterionIndex]
    }
}

const { width, height } = useWindowSize()
function getTileWidth() {
    return width.value > height.value ? "size-[20vh]" : "size-[20vw]"
}

</script>

<template>
    <div>
        <div class="grid grid-cols-5">
            <div v-for="index in [...Array(25).keys()]">
                <Tile 
                    v-if="gridIndexToPokeIndex(index) >= 0"
                    :index="gridIndexToPokeIndex(index)"
                    :key="pokemonNames[gridIndexToPokeIndex(index)]" 
                    :name="pokemonNames[gridIndexToPokeIndex(index)]" 
                    @click="handleShowSearch(gridIndexToPokeIndex(index))"
                />
                <Criterion 
                    v-else-if="gridIndexToCriterionIndex(index) >= 0"
                    :class="getTileWidth()" 
                    :criterion="getCriterion(index)"
                />
                <!-- Empty box to align remaining cells properly -->
                <div v-else></div>
            </div>
        </div>
    </div>
    <Search v-if="searchIndex >= 0" @click="handleCloseSearch" />

</template>
