# 📝 To-Do List Application (Python)

A simple command-line **To-Do List Application** built with Python that helps users manage their daily tasks. Users can add, view, remove, and mark tasks as completed. All tasks are automatically saved in a JSON file, so they remain available even after closing the program.

---

## 📌 Features

* ➕ Add new tasks
* 📋 View all tasks
* ❌ Remove tasks
* ✅ Mark tasks as completed
* 💾 Automatically save tasks using a JSON file
* 🔄 Load saved tasks when the program starts
* 🛡️ Handles invalid inputs using exception handling

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📂 Project Structure

```text
To-Do-List-in-Python/
│── To-Do-List.py          # Main Python program
│── tasks.json       # Stores tasks (created automatically)
│── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/nidaarshad-arch/To-Do-List-in-Python
```

2. Open the project folder.

3. Run the program:

```bash
python To-Do-List.py
```

---

## 📖 How It Works

When you start the program, you'll see the following menu:

```text
====== MENU FOR TO-DO-LIST ======
1. Add Task
2. View Task
3. Remove Task
4. Mark the Task as Done
5. Exit
```

Choose an option by entering the corresponding number.

* **Add Task** – Adds a new task with a default status of **Pending**.
* **View Task** – Displays all tasks along with their current status.
* **Remove Task** – Deletes a task by its task number.
* **Mark Task as Done** – Changes a task's status from **Pending** to **Done**.
* **Exit** – Closes the application.

---

## 💾 Data Storage

Tasks are stored in a file named `tasks.json`.

Example:

```json
[
    {
        "Task": "Complete Python project",
        "Status": "Pending"
    },
    {
        "Task": "Read a book",
        "Status": "Done"
    }
]
```

The application automatically:

* Saves tasks after every change.
* Loads previously saved tasks whenever the program starts.

---

## 🧠 Python Concepts Used

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling (`try` / `except`)
* File Handling
* JSON Module
* User Input
* String Formatting (f-strings)

---

## 🚀 Future Improvements

Some features that can be added in future versions:

* ✏️ Edit existing tasks
* 🔍 Search for a task
* 📅 Add due dates
* ⭐ Set task priorities
* 🗂️ Filter completed and pending tasks
* 🗑️ Delete all completed tasks
* 🎨 Build a graphical interface using Tkinter or CustomTkinter

---

## 📷 Sample Output

```text
====== MENU FOR TO-DO-LIST ======

1. Add Task
2. View Task
3. Remove Task
4. Mark the Task as Done
5. Exit

Choose what task you want to perform (1-5): 2

======= Your To-Do List =======

1. Study Python - Pending
2. Complete Assignment - Done
```

---

## 🎯 Learning Objectives

This project was built to practice:

* Writing modular Python programs using functions.
* Working with lists and dictionaries.
* Reading from and writing to JSON files.
* Handling user input safely with exception handling.
* Building a real-world beginner Python application.

---

## 👩‍💻 Author

**Nida Arshad**

If you found this project helpful, feel free to ⭐ star the repository and explore my other Python projects!

