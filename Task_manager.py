# Simple Task Manager Program
# Allows users to add, view/check/uncheck, and remove tasks

# Lists to store tasks and their status
tasks = []
checkbox = []

# Function to add a new task
def add_task():
    task = input("Create your task: ")
    tasks.append(task)
    checkbox.append("[x]")

# Function to view tasks and toggle their status
def view_tasks():
    if not tasks:
        print("\nYou don't have any tasks to view.")
        return

    while True:
        print("\n=== Tasks ===")
        for i, (task, box) in enumerate(zip(tasks, checkbox), start=1):
            print(f"{i}. {task} {box}")
        print("Type [0] to exit.")

        try:
            choice = int(input("\nSelect task to check/uncheck: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 0:
            break

        elif 1 <= choice <= len(tasks):
            index = choice - 1
            checkbox[index] = "[✓]" if checkbox[index] == "[x]" else "[x]"
        else:
            print("Invalid task number. Try again.")

# Function to remove tasks
def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    print("Choose which task to remove:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    try:
        choice = int(input("Which task do you wish to remove?: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            checkbox.pop(choice - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Main function and output menu
def main():
    while True:
        try:
            select = int(input("\n=== Task Manager ===\n1.Add Task\n2.View Tasks\n3.Remove Task\n4.Exit\n\nSelect: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == 1:
            add_task()
        elif select == 2:
            view_tasks()
        elif select == 3:
            remove_task()
        elif select == 4:
            print("\nGoodbye see you later!")
            break
        else:
            print("Please select between the options.")

# Run the program
main()
