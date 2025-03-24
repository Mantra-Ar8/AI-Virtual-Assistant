# To-Do List App (Beginner Version)
tasks = []  # List to store tasks

def show_tasks():
    """Display all tasks"""
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task"""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    """Remove a task"""
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
