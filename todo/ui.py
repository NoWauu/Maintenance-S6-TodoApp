import streamlit as st
from .state import ensure_state, get_tasks
from .actions import add_task, toggle_task, delete_task

def render() -> None:
    ensure_state()
    st.title("Ma TodoList")

    with st.form(key="task_form", clear_on_submit=True):
        new_task = st.text_input("Ajouter une tâche", key="new_task")
        submitted = st.form_submit_button("Ajouter")
    if submitted:
        add_task(new_task)

    st.subheader("Liste des tâches")

    tasks = get_tasks()
    unfinished = []
    completed = []
    for i, t in enumerate(tasks):
        if t.get("done"):
            completed.append((i, t))
        else:
            unfinished.append((i, t))

    if not unfinished and not completed:
        st.info("Aucune tâche pour l'instant. Ajoutez-en une !")

    if unfinished:
        st.markdown("**À faire**")
        for i, t in unfinished:
            col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
            with col1:
                st.write(t["task"])
            with col2:
                st.button("Marquer comme fait", key=f"task_{i}", on_click=toggle_task, args=(i,), use_container_width=True)
                print("Après :", st.session_state["tasks"][index ])
            with col3:
                st.button("Supprimer", key=f"delete_task_{i}", on_click=delete_task, args=(i,), use_container_width=True)

    if completed:
        st.markdown("**Terminées**")
        with st.expander(f"Voir {len(completed)} tâches terminées", expanded=False):
            for i, t in completed:
                col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
                with col1:
                    st.markdown(f"~~{t['task']}~~")
                with col2:
                    st.button("Marquer comme non fait", key=f"task_done_{i}", on_click=toggle_task, args=(i,), use_container_width=True)
                with col3:
                    st.button("Supprimer", key=f"delete_done_{i}", on_click=delete_task, args=(i,), use_container_width=True)
