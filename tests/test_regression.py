import streamlit as st

from todo.actions import add_task, delete_task, toggle_task
from todo.state import get_tasks


def setup_function() -> None:
    st.session_state.clear()


def test_no_empty_tasks_regression() -> None:
    add_task("")
    add_task("   ")

    assert get_tasks() == []

def test_add_task_with_valid_text_regression() -> None:
    add_task("Faire les tests")

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Faire les tests"
    assert tasks[0]["done"] is False

def test_remove_task_with_valid_index_regression() -> None:
    add_task("Tâche 1")
    add_task("Tâche 2")

    delete_task(0)

    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Tâche 2"

def test_toggle_task_with_valid_index_regression() -> None:
    add_task("Faire le TP")

    toggle_task(0)

    assert get_tasks()[0]["done"] is True

def test_toggle_task_two_times_regression() -> None:
    add_task("Faire le TP")

    toggle_task(0)
    toggle_task(0)

    assert get_tasks()[0]["done"] is False