<script lang="ts">
    import NodeComponent from "./NodeComponent.svelte";
    import { afterUpdate } from "svelte";
    import ArrowComponent from "./ArrowComponent.svelte";

    export let hint: string | undefined = undefined;
    export let graphNames: string[];

    let scrollContainer: HTMLDivElement;
    afterUpdate(() => {
        if (scrollContainer) {
            scrollContainer.scrollTo({
                left: scrollContainer.scrollWidth,
                behavior: "smooth"
            });
        }
    });
</script>

<div
    class="bg-red-400 w-3/4 min-h-[180px] h-[180px] rounded-lg border-black border-2"
>
    <div
        bind:this={scrollContainer}
        class="h-full flex items-center px-4 overflow-x-auto whitespace-nowrap"
    >
        {#each graphNames as name, i}
            {#if i}
                <ArrowComponent />
            {/if}
            <NodeComponent pokemonName={name} />
        {/each}
        {#if hint}
            <ArrowComponent />
            <NodeComponent pokemonName={hint} isSecret={true} />
        {/if}
    </div>
</div>
