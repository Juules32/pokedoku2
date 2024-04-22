<script setup lang="ts">
import TypeIcon from './TypeIcon.vue';
defineProps<{
    criteriaCategory: string
    criteriaContent: string
}>()


function parseCriteria(criteriaCategory: string, criteriaContent: string) {
    return `${criteriaCategory}: ${criteriaContent}`
}

</script>

<template>
    <!-- make this prettier -->    
    <div class="size-40 flex justify-center items-center">
        <TypeIcon v-if="criteriaCategory == 'type'" :type="criteriaContent" />
        <a v-else class="capitalize text-xl">{{ parseCriteria(criteriaCategory, criteriaContent) }}</a>
    </div>
</template>
