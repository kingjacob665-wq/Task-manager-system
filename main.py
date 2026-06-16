from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []

while True:
    print("\n===== Task Management System =====")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        add_task(tasks, title, description, due_date)

    elif choice == "2":
        title = input("Enter task title to complete: ")
        mark_task_as_complete(tasks, title)

    elif choice == "3":
        pending_tasks = view_pending_tasks(tasks)
        if len(pending_tasks) == 0:
            print("No pending tasks")
        else:
            for task in pending_tasks:
                print(task)

    elif choice == "4":
        progress = calculate_progress(tasks)
        print(f"Progress: {progress:.2f}%")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")