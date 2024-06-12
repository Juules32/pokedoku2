<script setup lang="ts">
defineProps<{
    type: string
}>()

const BASE_URL = import.meta.env.BASE_URL
</script>

<template>
    <img class="w-16" :src="`${BASE_URL}assets/types/type-${type}.png`" :alt="type" />
</template>

<style scoped>
img {
    image-rendering: pixelated
}
</style>