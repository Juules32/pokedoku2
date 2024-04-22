<script setup lang="ts">
import { RouterView } from 'vue-router'
import { pokemonNames } from './utils/userState';
import { watch } from 'vue';

watch(pokemonNames, newNames => {
    if (newNames.every(name => name != "")) {
        alert("You won!");
    }
});

</script>

<template>
  <RouterView class="font-undertale"/>
</template>
