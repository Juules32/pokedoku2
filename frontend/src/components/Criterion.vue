<script setup lang="ts">
import TypeIcon from './TypeIcon.vue';
defineProps<{
    category: string
}>()

function parseCategory(category: string) {

    const special_categories = ["mono-type", "dual-type", "ultra-beast"]

    if (special_categories.indexOf(category) > -1) {
        return category.replace("-", " ")
    }

    const split_category = category.split("-")
    if (split_category.length > 1) {
        
        return `${split_category[0]}: ${split_category[1]}`
    }
    return category
}

function isType(category: string) {
    return category.startsWith("type-")
}

function getType(category: string) {
    return category.split("-")[1]
}

</script>

<template>
    <!-- make this prettier -->    
    <div class="flex justify-center items-center">
        <TypeIcon v-if="isType(category)" :type="getType(category)" />
        <a v-else class="capitalize text-xl">{{ parseCategory(category) }}</a>
    </div>
</template>
