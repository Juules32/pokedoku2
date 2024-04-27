<script lang="ts" setup>
import axios from 'axios'
import { ref } from 'vue'

const props = defineProps<{
    name: string
    index: number
}>()

const name = ref(props.name)
const pokedexNumber = ref(null)
const spriteUrl = ref("")
const apiURL = `https://pokeapi.co/api/v2/pokemon/${name.value.toLowerCase()}`

async function getInformationFromAPI() {
    try {
        const response = await axios.get(apiURL);
        if (!response.data) {
            throw new Error('Response data not found');
        }
        name.value = response.data.name
        pokedexNumber.value = response.data.id,
        spriteUrl.value = response.data.sprites.front_default
    } catch (error) {
        console.error(error)
    }
}

if (name.value) {
    getInformationFromAPI()
}

</script>

<template> 
    
    <div class="size-full bg-white flex justify-center items-center border-black border relative"
        :class="{
            ['rounded-tl-xl']: index==0,
            ['rounded-tr-xl']: index==2,
            ['rounded-bl-xl']: index==6,
            ['rounded-br-xl']: index==8
        }"
    >
        <img v-if="spriteUrl" :src=spriteUrl class="size-full"/>
        <p v-if="pokedexNumber" class="absolute top-0 left-0 right-0 text-center">#{{ pokedexNumber }}</p>
        <p class="absolute bottom-0 left-0 right-0 text-center capitalize">{{ name }}</p>
    </div>
</template>