<script setup lang="ts">
import Grid from '../components/Grid.vue'
import VictoryText from '../components/VictoryText.vue';

function getRandomBackgroundPath() {
	const backgroundNames: string[] = [
		"forest",
		"berry-forest",
		"cave",
		"cave2",
		"cave3",
		"cave4",
		"chamber",
		"hideout",
		"mansion",
		"mt-ember",
		"power-plant",
		"safari",
		"tower",
		"tower2",
		"victory-road",
		"warehouse"
	]
	return `${import.meta.env.BASE_URL}assets/backgrounds/${backgroundNames[Math.floor(Math.random() * backgroundNames.length)]}.png`
}

</script>

<template>
	<main>
		<div 
			class="fixed inset-0 flex flex-col justify-center items-center bg-center bg-cover" 
			:style="{ 
				'background-image': 'url(' + getRandomBackgroundPath() + ')',
				'image-rendering': 'pixelated'
			}"
		>
			<VictoryText />
			<Grid />
		</div>
	</main>
</template>
<style scoped>
img {
    image-rendering: pixelated
}
</style>