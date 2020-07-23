# Named entity selection in Streamlit + Svelte

Time to test Svelte + Streamlit Component on some Prodigy demo !

## Setup

- Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
- Clone this repo.
- Create a new Python virtual environment for the template:

```
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```

- Initialize and run the component template frontend:

```
$ cd streamlit_named_entity/frontend
$ npm install    # Install npm dependencies
$ npm run dev  # Start the Webpack dev server
```

- From a separate terminal, run the template's Streamlit app:

```
$ . venv/bin/activate  # activate the venv you created earlier
$ streamlit run streamlit_named_entity/__init__.py  # run the example
```

- If all goes well, you should see something like this:
  ![Quickstart Success](quickstart.png)
- Modify the frontend code at `streamlit_named_entity/frontend/`.
- Modify the Python code at `streamlit_named_entity/__init__.py`.

## References

- [Prodigy demo](https://prodi.gy/)
