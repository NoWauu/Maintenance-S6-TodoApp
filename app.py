# fichier : app.py
import streamlit as st

# Stockage des tâches en mémoire (disparaît si on relance l'app)
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Ma TodoList")

# Ajouter une nouvelle tâche
new_task = st.text_input("Ajouter une tâche")
if st.button("Ajouter"):
    if new_task.strip() != "":
        st.session_state["tasks"].append({"task": new_task, "done": False})

# Afficher les tâches en cours
st.subheader("Liste des tâches")
unfinished_tasks = [t for t in st.session_state["tasks"] if not t["done"]]
if unfinished_tasks:
    for i, t in enumerate(st.session_state["tasks"]):
        if not t["done"]:
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(t["task"])
            with col2:
                if st.button("Marquer comme fait", key=f"done_{i}"):
                    st.session_state["tasks"][i]["done"] = True
else:
    st.info("Aucune tâche en cours.")

# Afficher les tâches terminées dans un accordéon
completed_tasks = [t for t in st.session_state["tasks"] if t["done"]]
with st.expander("Tâches terminées"):
    if completed_tasks:
        for t in completed_tasks:
            st.write(t["task"])
    else:
        st.write("Aucune tâche terminée.")

# Lancer l'application avec : streamlit run app.py