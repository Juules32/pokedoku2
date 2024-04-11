<script lang="ts" setup>
const props = defineProps<{
    name: string
    spriteUrl: string
}>()
</script>

<template>
    <div class="flex items-center p-2">

        <img :src="spriteUrl" />
        <p class="grow text-left pl-2">{{ name }}</p>
        <button class="btn bg-red-400">Guess</button>
    </div>
</template>