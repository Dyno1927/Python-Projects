# Imports #
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Tk Window Setup #
root = tk.Tk()
root.title("To-Do List")

tk.Label(root, text="Task").grid(row=0, column=0)
tk.Label(root, text="From-Time").grid(row=1, column=0)
tk.Label(root, text="To-Time").grid(row=2, column=0)

task_entry = tk.Entry(root)
task_entry.grid(row=0, column=1)

from_time_entry = tk.Entry(root)
from_time_entry.grid(row=1, column=1)

to_time_entry = tk.Entry(root)
to_time_entry.grid(row=2, column=1)

# Defined Functions #
def add_task():
    task = task_entry.get().strip()
    from_time = from_time_entry.get().strip()
    to_time = to_time_entry.get().strip()

    if not task:
        messagebox.showwarning("Task", "Please enter a task.")
        return

    try:
        from_hours, from_minutes = map(int, from_time.split(":"))
        total_minutes_from = from_hours * 60 + from_minutes
    except ValueError:
        messagebox.showwarning("From-Time", "Please enter time in HH:MM format.")
        return

    try:
        to_hours, to_minutes = map(int, to_time.split(":"))
        total_minutes_to = to_hours * 60 + to_minutes
    except ValueError:
        messagebox.showwarning("To-Time", "Please enter time in HH:MM format.")
        return

# Tree View / List #
    tree.insert("", "end", values=(task, f"{from_hours}:{from_minutes:02d}", f"{to_hours}:{to_minutes:02d}"))

    task_entry.delete(0, tk.END)
    from_time_entry.delete(0, tk.END)
    to_time_entry.delete(0, tk.END)

tree = ttk.Treeview(root, columns=("Task", "From-Time", "To-Time"), show="headings")
tree.heading("Task", text="Task")
tree.heading("From-Time", text="From-Time")
tree.heading("To-Time", text="To-Time")
tree.grid(row=4, column=0, columnspan=2)

# Json Save & Load Thingy #
def save_tasks():
    tasks = []
    for item in tree.get_children():
        values = tree.item(item, "values")
        tasks.append(values)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

    for item in tree.get_children():
        tree.delete(item)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                tree.insert("", "end", values=task)
    except FileNotFoundError:
        pass

tk.Button(root, text="Add Task", command=add_task).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Save Tasks", command=save_tasks).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Load Tasks", command=load_tasks).grid(row=6, column=0, columnspan=2)

load_tasks()
root.mainloop()
