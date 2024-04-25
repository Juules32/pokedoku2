<script setup lang="ts">
import { pokemonNames } from '../utils/userState';

function youWon() {
	return pokemonNames.every(name => name != "")
}

</script>

<template>
	<h1 class="text-3xl" v-if="youWon()">👺 You Won! 👺</h1>
</template>
