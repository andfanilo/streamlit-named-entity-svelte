import os
import spacy
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_named_entity",
        url="http://localhost:5000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_named_entity", path=build_dir)

def st_named_entity_demo(text, ents, key=None):
    entities = _component_func(text=text, ents=ents, key=key, default=ents)
    return entities

if not _RELEASE:
    import streamlit as st

    st.title("Named entity recognition demo")
    text = "Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002 by Me."
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ents = doc.to_json()['ents']
    entities = st_named_entity_demo(text, ents, key=42)
    st.json(entities)
