tasks = []

def display_menu():
    """Prints the main menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")
    print("-----------------------")

def add_task():
    """Prompts the user for a task and adds it to the list."""
    task_description = input("Enter the task you want to add: ").strip()
    if task_description: # Check if the input is not empty
        # Store the task as a dictionary with description and completed status
        new_task = {'description': task_description, 'completed': False}
        tasks.append(new_task)
        print(f"'{task_description}' has been added to your to-do list.")
    else:
        print("Task description cannot be empty. Please try again.")

def view_tasks():
    """Displays all tasks in the list, with their numbers and completion status."""
    if not tasks: # Check if the list is empty
        print("Your to-do list is empty. Add some tasks!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks):
            status_box = "[X]" if task['completed'] else "[ ]" # [X] if done, [ ] if not

            # Get the task description
            original_task_text = task['description']
            display_text = original_task_text

            if task['completed']:
                # Step 1: Join characters with a hyphen
                # Example: "Work" -> "W-o-r-k"
                hyphenated_text = "-".join(original_task_text.upper()) # Using .upper() for consistency with example

                # Step 2: Add leading and trailing hyphens as per your example
                display_text = f"-----{hyphenated_text}-----"
            
            print(f"{index + 1}. {status_box} {display_text}")
        print("------------------")

def mark_task_complete():
    """Allows the user to mark a task as complete by its number."""
    view_tasks() # Show tasks first so the user knows the numbers
    if not tasks:
        return # Exit if there are no tasks to mark

    try:
        task_num_str = input("Enter the number of the task to mark as complete: ")
        task_number = int(task_num_str) # Convert input to an integer

        # Adjust for 0-based indexing (user enters 1, list uses 0)
        task_index = task_number - 1

        if 0 <= task_index < len(tasks): # Check if the number is valid
            if not tasks[task_index]['completed']: # Only mark if not already complete
                tasks[task_index]['completed'] = True # Set the 'completed' flag to True
                print(f"Task '{tasks[task_index]['description']}' marked as complete.")
            else:
                print(f"Task '{tasks[task_index]['description']}' is already complete.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    """Allows the user to delete a task by its number."""
    view_tasks() # Show tasks first so the user knows the numbers
    if not tasks:
        return # Exit if there are no tasks to delete

    try:
        task_num_str = input("Enter the number of the task to delete: ")
        task_number = int(task_num_str)

        # Adjust for 0-based indexing
        task_index = task_number - 1

        if 0 <= task_index < len(tasks):
            removed_task_dict = tasks.pop(task_index) # .pop() removes and returns the dict
            print(f"Task '{removed_task_dict['description']}' has been deleted.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# --- Main program loop ---
def run_todo_list():
    """Main function to run the To-Do List application."""
    print("Welcome to your Command-Line To-Do List!")

    while True: # This loop keeps the program running until you choose to quit
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break # Exit the while loop, which ends the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This line calls the main function to start the program
if __name__ == "__main__":
    run_todo_list()
