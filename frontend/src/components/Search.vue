<script lang="ts" setup>
import { onMounted, ref, watch } from 'vue'
import { getSearchData } from '../utils/pokeAPI';
import SearchResult from './SearchResult.vue';

const search = ref("")
const filteredPokemon = ref([])

watch(search, async newValue => {
    filteredPokemon.value = await getSearchData(newValue)
});

onMounted(() => {
    document.getElementById('searchInput').focus()
})

</script>

<template>
    <div 
        id="background" 
        class="fixed inset-0 flex justify-center transition-colors bg-black/20"
    >
        <div class="w-[500px] mt-32 h-fit">

            <div class="bg-red-400 h-16 flex border-2 border-b-0 border-black justify-center items-center rounded-t-lg">
                <input 
                    id="searchInput" 
                    class="p-2 w-72 border-2 border-black" 
                    type="text" 
                    v-model="search"
                    placeholder="Search for a pokemon..."
                >
            </div>
            <ul class="divide-y divide-dashed h-96 overflow-y-auto border-2 border-black bg-white rounded-b-lg">
                <li v-for="pokemon in filteredPokemon" class="hover:bg-gray-200">
                    <SearchResult 
                        :spriteUrl="pokemon.spriteUrl" 
                        :name="pokemon.name"
                    />
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background-color: #f1f1f1;
    border-radius: 10px;
    /* Rounded corners */
}

::-webkit-scrollbar-thumb {
    background-color: #888;
    border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
    background-color: #555;
}
</style>
