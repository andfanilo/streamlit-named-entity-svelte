import os
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

def st_named_entity_demo(name, key=None):
    component_value = _component_func(name=name, key=key, default=0)
    return component_value

if not _RELEASE:
    import streamlit as st

    st.title("Named entity recognition demo")
    num_clicks = st_named_entity_demo("World")
