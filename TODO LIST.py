import sys

# Initialize an empty to-do list
todo_list = []

# Function to display the to-do list
def display_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = 'Done' if task['completed'] else 'Pending'
            print(f"{i}. {task['task']} - {status}")
    print()

# Function to add a new task
def add_task():
    task_name = input("Enter the task: ")
    todo_list.append({'task': task_name, 'completed': False})
    print(f"Task '{task_name}' added to your to-do list!\n")

# Function to update a task
def update_task():
    display_todo_list()
    if not todo_list:
        return

    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print(f"Task '{todo_list[task_num - 1]['task']}' marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Function to delete a task
def delete_task():
    display_todo_list()
    if not todo_list:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted from your to-do list!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Function to display the menu
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Main loop for the application
def main():
    print("Welcome to the To-Do List Application!")  # Added welcome message
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please select an option between 1 and 5.\n")

# Entry point for the script
if __name__ == "__main__":
    main()  # Make sure the main function is called
