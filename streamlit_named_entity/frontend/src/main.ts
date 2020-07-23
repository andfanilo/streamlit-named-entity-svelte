import App from "./App.svelte";

const app = new App({
  target: document.body,
  props: {
    text:
      "Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002 by Me",
    ents: [
      {
        start: 0,
        end: 6,
        label: "ORG",
      },
      {
        start: 22,
        end: 36,
        label: "DATE",
      },
      {
        start: 40,
        end: 50,
        label: "PERSON",
      },
      {
        start: 55,
        end: 66,
        label: "PERSON",
      },
      {
        start: 83,
        end: 88,
        label: "WORK_OF_ART",
      },
      {
        start: 101,
        end: 120,
        label: "ORG",
      },
      {
        start: 124,
        end: 134,
        label: "GPE",
      },
      {
        start: 154,
        end: 170,
        label: "PERCENT",
      },
      {
        start: 197,
        end: 207,
        label: "PERCENT",
      },
      {
        start: 285,
        end: 291,
        label: "ORG",
      },
      {
        start: 297,
        end: 307,
        label: "GPE",
      },
      {
        start: 334,
        end: 351,
        label: "DATE",
      },
      {
        start: 356,
        end: 366,
        label: "GPE",
      },
      {
        start: 368,
        end: 374,
        label: "ORG",
      },
      {
        start: 402,
        end: 410,
        label: "GPE",
      },
      {
        start: 414,
        end: 430,
        label: "DATE",
      },
    ],
  },
});

export default app;
