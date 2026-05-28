# fichier : app.py
import streamlit as st

# Stockage des tâches en mémoire (disparaît si on relance l'app)
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []


def toggle_task(task_index):
    """Bascule l'état d'une tâche."""
    st.session_state["tasks"][task_index]["done"] = not st.session_state["tasks"][task_index]["done"]

st.title("Ma TodoList")

# Ajouter une nouvelle tâche
new_task = st.text_input("Ajouter une tâche")
if st.button("Ajouter"):
    if new_task.strip() != "":
        st.session_state["tasks"].append({"task": new_task, "done": False})

# Afficher les tâches en cours
st.subheader("Liste des tâches")
completed_tasks = []
unfinished_found = False
for i, t in enumerate(st.session_state["tasks"]):
    if t["done"]:
        completed_tasks.append(t)
        continue

    unfinished_found = True
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(t["task"])
    with col2:
        button_label = "Marquer comme non fait" if t["done"] else "Marquer comme fait"
        st.button(button_label, key=f"task_{i}", on_click=toggle_task, args=(i,))

if not unfinished_found:
    st.info("Aucune tâche en cours.")

# Afficher les tâches terminées dans un accordéon
with st.expander("Tâches terminées"):
    if completed_tasks:
        for t in completed_tasks:
            st.write(t["task"])
    else:
        st.write("Aucune tâche terminée.")

# Lancer l'application avec : streamlit run app.py