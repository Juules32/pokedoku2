<script lang="ts" setup>
import axios from 'axios'
import { ref } from 'vue'
import { capitalize } from '../utils/stringManip.ts'
const props = defineProps<{
    name: string
}>()



const name = ref(capitalize(props.name))
const pokedexNumber = ref(null)
const spriteUrl = ref("")
const apiURL = `https://pokeapi.co/api/v2/pokemon/${name.value.toLowerCase()}`

async function getInformationFromAPI() {
    try {
        const response = await axios.get(apiURL);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        name.value = capitalize(response.data.name)
        pokedexNumber.value = response.data.id,
        spriteUrl.value = response.data.sprites.front_default
    } catch (error) {
    }
}

getInformationFromAPI()

</script>

<template> 
    <div class="flex justify-center items-center size-40 border-current border relative">
        <img :src=spriteUrl />
        <p class="absolute top-0 left-0 right-0 text-center">#{{ pokedexNumber }}</p>
        <p class="absolute bottom-0 left-0 right-0 text-center">{{ name }}</p>
    </div>
</template>