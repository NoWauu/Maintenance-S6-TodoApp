# fichier : app.py
import streamlit as st

# Stockage des tâches en mémoire (disparaît si on relance l'app)
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []


def toggle_task(task_index):
    """Bascule l'état d'une tâche."""
    st.session_state["tasks"][task_index]["done"] = not st.session_state["tasks"][task_index]["done"]

def delete_task(task_index):
    """Supprime une tâche."""
    st.session_state["tasks"].pop(task_index)    
    

def add_task():
    """Ajoute une nouvelle tâche et vide l'input."""
    new_task = st.session_state["new_task"].strip()
    if new_task != "":
        st.session_state["tasks"].append({"task": new_task, "done": False})
    st.session_state["new_task"] = ""

st.title("Ma TodoList")

# Ajouter une nouvelle tâche
new_task = st.text_input("Ajouter une tâche")
if st.button("Ajouter"):
    if new_task.strip() != "":
        st.session_state["tasks"].append({"task": new_task, "done": False})
if "new_task" not in st.session_state:
    st.session_state["new_task"] = ""

st.text_input("Ajouter une tâche", key="new_task")
st.button("Ajouter", on_click=add_task)

# Afficher les tâches
st.subheader("Liste des tâches")
for i, t in enumerate(st.session_state["tasks"]):
    if t["done"]:
        completed_tasks.append(t)
        continue

    unfinished_found = True
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    with col1:
        st.write(("Terminé - " if t["done"] else "À faire - ") + t["task"])
    with col2:
        button_label = "Marquer comme non fait" if t["done"] else "Marquer comme fait"
        st.button(button_label, key=f"task_{i}", on_click=toggle_task, args=(i,), use_container_width=True)
    with col3:
        st.button("Supprimer", key=f"delete_task_{i}", on_click=delete_task, args=(i,), use_container_width=True)

# Lancer l'application avec : streamlit run app.py
