# Simple To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
