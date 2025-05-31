# Enhanced Command-Line To-Do List Application

This is an interactive to-do list application built purely in Python, designed to run in your command line or terminal. It offers standard task management features but includes a **unique visual flair** for completed items, making it easy to distinguish your progress.

This project is great for beginners to understand core Python concepts like lists, dictionaries, loops, conditional statements, and user input/output in a practical, fun way.

## ✨ Features

* **Add Task:** Easily add new to-do items to your list.
* **View Tasks:** Display all current tasks with their corresponding numbers and completion status.
* **Mark Task as Complete:** Mark a task as done by its number. **Completed tasks are visually "crossed out" with a distinct hyphenated format (e.g., `---W-O-R-K-----`) and marked with `[X]`.**
* **Delete Task:** Remove a task from the list using its number.
* **User-Friendly Interface:** Simple numbered menu for easy navigation.
* **In-Memory Storage:** Tasks are stored as long as the application is running (they are cleared when the program exits).

## 📊 How Completed Tasks Look

When you mark a task like "Work" as complete, it will transform from `[ ] Work` to something like:

`[X] ---W-O-R-K-----`

This provides a clear and unique visual indicator of completion.

## 🚀 How to Use

To run this To-Do List application, you'll need Python installed on your computer.

### Prerequisites

* [Python 3.x](https://www.python.org/downloads/) (Ensure you have a recent version of Python 3 installed.)

### Running the Application

1.  **Save the code:**
    * Save the Python code for the To-Do List into a file named `todo_list.py`.
    * Place this file in a convenient folder on your computer (e.g., `Documents/PythonProjects/todo-app`).

2.  **Open your Command Prompt / Terminal:**
    * **On Windows:** Navigate to the folder where you saved `todo_list.py` in File Explorer. Click on the address bar at the top, type `cmd`, and press `Enter`.
    * **On Mac/Linux:** Open your Terminal application. Use the `cd` command to navigate to the directory where your `todo_list.py` file is located. For example: `cd ~/Documents/PythonProjects/todo-app`.

3.  **Execute the Python script:**
    * Once you are in the correct directory in your Command Prompt/Terminal, type the following command and press `Enter`:
        ```bash
        python todo_list.py
        ```

4.  **Interact with the To-Do List:**
    * The application will start, display a menu, and prompt you for a choice.
    * Type the number corresponding to the action you want to perform (e.g., `1` to add a task, `2` to view tasks).
    * Follow the on-screen instructions.
    * To exit the application, type `5` and press `Enter`.

## 🧠 Concepts Demonstrated

* `list` data structure for storing multiple tasks.
* `dictionary` data structure for storing task details (description and completion status).
* `while` loops for continuous program execution.
* `if`/`elif`/`else` for menu navigation and conditional logic.
* `input()` for user interaction.
* `print()` for displaying information.
* String methods (`.strip()`, `.upper()`, `.join()`) for text manipulation and formatting.
* Basic error handling (`try-except` for number input, `if` statements for valid choices/numbers).
* Functions (`def`) for organizing code into reusable blocks.

## 🤝 Contributing

This project is a fantastic starting point for learning Python. Feel free to explore the code, make modifications, and enhance its features! Suggestions and improvements are always welcome.

## 📄 License

This project is open-source and available under the MIT License.

---
