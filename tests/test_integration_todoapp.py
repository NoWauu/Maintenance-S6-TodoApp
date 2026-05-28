from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parents[1] / "main.py"


def launch_app() -> AppTest:
    app = AppTest.from_file(str(APP_PATH))
    app.run()
    return app


def add_task(app: AppTest, task: str) -> None:
    app.text_input[0].set_value(task)
    app.button[0].click()
    app.run()


def test_initial_render_shows_empty_state() -> None:
    app = launch_app()

    assert [title.value for title in app.title] == ["Ma TodoList"]
    assert [subheader.value for subheader in app.subheader] == ["Liste des tâches"]
    assert [info.value for info in app.info] == ["Aucune tâche pour l'instant. Ajoutez-en une !"]
    assert [button.label for button in app.button] == ["Ajouter"]
    assert [text_input.label for text_input in app.text_input] == ["Ajouter une tâche"]
    assert app.session_state["tasks"] == []


def test_adding_task_creates_a_pending_item() -> None:
    app = launch_app()

    add_task(app, "Buy milk")

    assert app.session_state["tasks"] == [{"task": "Buy milk", "done": False}]
    assert [markdown.value for markdown in app.markdown] == ["**À faire**", "Buy milk"]
    assert [button.label for button in app.button] == ["Ajouter", "Marquer comme fait", "Supprimer"]
    assert len(app.info) == 0


def test_marking_task_complete_moves_it_to_completed_section() -> None:
    app = launch_app()

    add_task(app, "Buy milk")
    app.button[1].click()
    app.run()

    assert app.session_state["tasks"] == [{"task": "Buy milk", "done": True}]
    assert [markdown.value for markdown in app.markdown] == ["**Terminées**", "~~Buy milk~~"]
    assert len(app.expander) == 1
    assert app.expander[0].label == "Voir 1 tâches terminées"
    assert [button.label for button in app.button] == [
        "Ajouter",
        "Marquer comme non fait",
        "Supprimer",
    ]


def test_deleting_task_clears_it_from_state_and_ui() -> None:
    app = launch_app()

    add_task(app, "Buy milk")
    app.button[2].click()
    app.run()

    assert app.session_state["tasks"] == []
    assert [info.value for info in app.info] == ["Aucune tâche pour l'instant. Ajoutez-en une !"]
    assert [button.label for button in app.button] == ["Ajouter"]
