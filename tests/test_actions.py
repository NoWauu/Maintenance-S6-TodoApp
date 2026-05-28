import streamlit as st

from todo.actions import add_task, toggle_task, delete_task
from todo.state import get_tasks

def setup_function():
    st.session_state.clear()

# Tests pour les fonctions d'action 
def test_add_task_adds_valid_task():
    add_task("Faire les tests")

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Faire les tests"
    assert tasks[0]["done"] is False

# Les tâches vides ou composées uniquement d'espaces ne doivent pas être ajoutées
def test_add_task_ignores_empty_text():
    add_task("")
    add_task("   ")

    assert get_tasks() == []

# Les tâches doivent être ajoutées même si elles contiennent des espaces avant ou après le texte
def test_toggle_task_changes_done_status():
    add_task("Faire le TP")

    toggle_task(0)

    assert get_tasks()[0]["done"] is True

# Les indices invalides ne doivent pas provoquer d'erreur et ne doivent pas modifier les tâches
def test_toggle_task_ignores_invalid_index():
    add_task("Faire le TP")

    toggle_task(99)
    toggle_task(-1)

    assert len(get_tasks()) == 1
    assert get_tasks()[0]["done"] is False

# Les tâches doivent être supprimées correctement
def test_delete_task_removes_task():
    add_task("Tâche 1")
    add_task("Tâche 2")

    delete_task(0)

    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Tâche 2"

# Les indices invalides ne doivent pas provoquer d'erreur et ne doivent pas modifier les tâches
def test_delete_task_ignores_invalid_index():
    add_task("Tâche 1")

    delete_task(99)
    delete_task(-1)

    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Tâche 1"