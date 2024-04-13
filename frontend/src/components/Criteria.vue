<script setup lang="ts">
defineProps<{
    criteriaName: string
}>()
</script>

<template>
    <!-- make this prettier -->    
    <div class="size-40 flex justify-center items-center">{{ criteriaName }}</div>
</template>