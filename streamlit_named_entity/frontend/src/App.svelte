<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import { Streamlit } from "./streamlit/streamlit";
  import type { RenderData } from "./streamlit/streamlit";
  import Word from "./components/Word.svelte";
  import MarkedWord from "./components/MarkedWord.svelte";

  let text: string = "";
  let ents: {
    start: number;
    end: number;
    label: string;
  }[] = [];

  const onRender = (event: Event): void => {
    const data = (event as CustomEvent<RenderData>).detail;
    text = data.args["text"];
    ents = data.args["ents"];
    Streamlit.setFrameHeight();
  };

  onMount(() => {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight();
    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
  });

  onDestroy(() => {
    Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRender);
  });
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
      <MarkedWord words={text.substring(start, end)} {label} />
      {#if i != ents.length - 1}
        {text.substring(end + 1, ents[i + 1]['start'] - 1)}
      {/if}
      {#if i == ents.length - 1}{text.substring(end)}{/if}
    {:else}
      <!-- this block renders when ents.length === 0 -->
      <p>loading...</p>
    {/each}
  </main>
</section>
