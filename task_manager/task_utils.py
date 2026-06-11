from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully")


def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            print("Task marked as complete")
            return

    print("Task not found")


def view_pending_tasks(tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    return pending_tasks


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    return (completed_tasks / len(tasks)) * 100