<script lang="ts">
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
  }
</style>

<section>
  <header>
    <h1>Named entity demo</h1>
  </header>
  <main>
    Hello
    <Entity word="Larry page" entity="PRODUCT" />
    Hello again
  </main>
</section>
