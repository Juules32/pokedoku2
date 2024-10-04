<script setup lang="ts">
import TypeIcon from './TypeIcon.vue';
defineProps<{
    criterion: string
}>()

function parseCriterion(criterion: string) {

    const special_criteria = ["mono-type", "dual-type", "ultra-beast"]

    if (special_criteria.includes(criterion)) {
        return criterion.replace("-", " ")
    }

    const split_criterion = criterion.split("-")
    if (split_criterion.length > 1) {
        
        return `${split_criterion[0]}: ${split_criterion[1]}`
    }
    return criterion
}

function isType(criterion: string) {
    return criterion.startsWith("type-")
}

function getType(criterion: string) {
    return criterion.split("-")[1]
}

</script>

<template>
    <!-- make this prettier -->    
    <div class="flex justify-center items-center">
        <TypeIcon v-if="isType(criterion)" :type="getType(criterion)" />
        <a v-else class="capitalize text-xl">{{ parseCriterion(criterion) }}</a>
    </div>
</template>
