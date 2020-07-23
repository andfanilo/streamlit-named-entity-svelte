<script lang="ts">
  export let word: string;
  export let entity: string;

  const colors = {
    ORG: "#7aecec",
    PRODUCT: "#bfeeb7",
    GPE: "#feca74",
    LOC: "#ff9561",
    PERSON: "#aa9cfc",
    NORP: "#c887fb",
    FACILITY: "#9cc9cc",
    EVENT: "#ffeb80",
    LAW: "#ff8197",
    LANGUAGE: "#ff8197",
    WORK_OF_ART: "#f0d0ff",
    DATE: "#bfe1d9",
    TIME: "#bfe1d9",
    MONEY: "#e4e7d2",
    QUANTITY: "#e4e7d2",
    ORDINAL: "#e4e7d2",
    CARDINAL: "#e4e7d2",
    PERCENT: "#e4e7d2",
  };
  const entityColor = `background-color: ${colors[entity] || "#ddd"}`;
</script>

<style>
  mark {
    display: inline-block;
    background-color: lightblue;
    padding: 0.45em 0.6em;
    margin: 0 0.25em;
    line-height: 1;
    border-radius: 0.35em;
    position: relative;
  }

  .entity {
    font-size: 0.8em;
    font-weight: bold;
    line-height: 1;
    text-transform: uppercase;
    vertical-align: middle;
    margin-left: 0.5rem;
  }

  .delete {
    top: -7px;
    left: -7px;
    color: #fff;
    width: 14px;
    height: 14px;
    display: flex;
    opacity: 0;
    z-index: 10;
    position: absolute;
    font-size: 0.7em;
    line-height: 1.1;
    text-align: center;
    background-color: #444;
    align-items: center;
    border-radius: 50%;
    justify-content: center;
    cursor: pointer;
    font-weight: bold;
    transition: opacity linear 0.1s;
  }

  mark:hover .delete {
    opacity: 1;
  }
</style>

<mark style={entityColor}>
  {word}
  <span class="entity">{entity}</span>
  <span class="delete">x</span>
</mark>
