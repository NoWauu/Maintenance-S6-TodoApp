import streamlit as st


def ensure_state():
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []


def get_tasks():
    ensure_state()
    return st.session_state["tasks"]
