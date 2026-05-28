from .state import ensure_state, get_tasks
import logging

logging.basicConfig(
    filename="logs/todo.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def add_task(text: str) -> None:
    ensure_state()
    if text and text.strip():
        get_tasks().append({"task": text, "done": False})
        logging.info(f"Task added: {text}")
    else:
        logging.warning(f"Attempt to add empty task")


def toggle_task(index: int) -> None:
    ensure_state()
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index].get("done", False)
        print("Après :", st.session_state["tasks"][index ])
        logging.info(f"{tasks[index]['done']} : Task toggled: {tasks[index]['task']}")


def delete_task(index: int) -> None:
    ensure_state()
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        logging.info(f"Task deleted: {task['task']}")
