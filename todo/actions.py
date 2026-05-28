from .state import ensure_state, get_tasks

def add_task(text: str) -> None:
    ensure_state()
    if text and text.strip():
        get_tasks().append({"task": text, "done": False})

def toggle_task(index: int) -> None:
    ensure_state()
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index].get("done", False)

def delete_task(index: int) -> None:
    ensure_state()
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
