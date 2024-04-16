<script setup lang="ts">
import TypeIcon from './TypeIcon.vue';
defineProps<{
    criteriaName: string
}>()


function parseCriteria(criteriaName: string) {
    if (criteriaName.startsWith("region")) {
        return `Region: ${criteriaName.split("-")[1]}`
    }
    else if (criteriaName.startsWith("knows")) {
        return `Knows ${criteriaName.split("-")[1]}`
    }

    return criteriaName
}

</script>

<template>
    <!-- make this prettier -->    
    <div class="size-40 flex justify-center items-center">
        <TypeIcon v-if="criteriaName.startsWith('type')" :type="criteriaName" />
        <a v-else class="capitalize text-xl">{{ parseCriteria(criteriaName) }}</a>
    </div>
</template>
