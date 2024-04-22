<script setup lang="ts">
defineProps<{
    type: string
}>()
</script>

<template>
    <img class="w-16" :src="`/assets/types/type-${type}.png`" :alt="type" />
</template>

<style scoped>
img {
    image-rendering: pixelated
}
</style>