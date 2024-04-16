<script setup lang="ts">
import Grid from '../components/Grid.vue'

function getRandomBackground() {
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
	const randomBackground = backgroundNames[Math.floor(Math.random() * backgroundNames.length)]
	return `/src/assets/backgrounds/${randomBackground}.png`
}
</script>

<template>
	<main>
		<div 
			class="fixed inset-0 flex justify-center items-center bg-center bg-cover" 
			:style="{ 
				'background-image': 'url(' + getRandomBackground() + ')',
				'image-rendering': 'pixelated'
			}"
		>
			<Grid />
		</div>
	</main>
</template>
<style scoped>
img {
    image-rendering: pixelated
}
</style>