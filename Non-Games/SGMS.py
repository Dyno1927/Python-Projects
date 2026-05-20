# imports #
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Defined Functions & Mark Calculations #
def marks_out_of_range(marks):
    return marks < 0 or marks > 80

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'D'
    elif marks < 33:
        return 'F'

def add_student():
    name = name_entry.get().strip()
    marks = marks_entry.get().strip()

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Invalid Name", "Please enter a valid name using letters only.")
        return

    try:
        marks_int = int(marks)
    except ValueError:
        messagebox.showerror("Invalid Marks", "Please enter a number for marks.")
        return

    if marks_out_of_range(marks_int):
        messagebox.showerror("Invalid Marks", "Marks must be between 0 and 80.")
        return

    grade = calculate_grade(marks_int)
    tree.insert("", "end", values=(name, marks_int, grade))

    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

def save_grades():
    grades = []
    for item in tree.get_children():
        values = tree.item(item, "values")
        grades.append(values)

    with open("grades.json", "w") as f:
        json.dump(grades, f)

    for item in tree.get_children():
        tree.delete(item)

def load_grades():
    try:
        with open("grades.json", "r") as f:
            grades = json.load(f)
            for grade in grades:
                tree.insert("", "end", values=grade)
    except FileNotFoundError:
        pass

# Tk Window Setup #
root = tk.Tk()
root.title("Student Grading Management System")

tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Marks").grid(row=1, column=0)
marks_entry = tk.Entry(root)
marks_entry.grid(row=1, column=1)

columns = ("Name", "Marks", "Grade")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
tree.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Add Student", command=add_student).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Save Grades", command=save_grades).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Load Grades", command=load_grades).grid(row=5, column=0, columnspan=2)

root.mainloop()
