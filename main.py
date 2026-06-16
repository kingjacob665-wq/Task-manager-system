def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Error: Task title cannot be empty.")
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Error: Task description cannot be empty.")
    return True

def validate_due_date(due_date):
    if len(due_date.strip()) == 0:
        raise ValueError("Error: Due date cannot be empty.")
    return True

def add_task(tasks, title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(e)
        return
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            print("Task marked as complete!")
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
