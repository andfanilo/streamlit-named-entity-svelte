<script lang="ts">
  export let text: string;
  export let ents: {
    start: number;
    end: number;
    label: string;
  }[];

  import Entity from "./components/Entity.svelte";
</script>

<style>
  section {
    padding: 1em;
  }
  header {
    background-color: rgb(88, 63, 207);
    color: #eee;
    padding: 0.1em 1em;
    margin-bottom: 1em;
  }
  main {
    padding: 1em;
    line-height: 2.5;
  }
</style>

<section>
  <header>
    <h1>Named entity demo</h1>
  </header>
  <main>
    {#each ents as { start, end, label }, i}
      {#if i == 0}{text.substring(0, start)}{/if}
      <Entity word={text.substring(start, end)} entity={label} />
      {#if i != ents.length - 1}
        {text.substring(end + 1, ents[i + 1]['start'] - 1)}
      {/if}
      {#if i == ents.length - 1}{text.substring(end)}{/if}
    {/each}
  </main>
</section>
