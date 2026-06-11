def validate_task_title(title):
    if len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    return True


def validate_task_description(description):
    if len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False
    return True


def validate_due_date(due_date):
    if len(due_date.strip()) == 0:
        print("Error: Due date cannot be empty.")
        return False
    return True