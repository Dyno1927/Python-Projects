# Imports #
import tkinter as tk
import math

# Set Variables #
memory = 0
angle_mode = "RAD"
history = []
dark_mode = False

# Exaluating Expressions & Allowed Thingys #
def evaluate_expression():
    global angle_mode
    expr = entry.get()

    while expr.count(")") > expr.count("("):
        expr = expr[:-1]
    while expr.count("(") > expr.count(")"):
        expr += ")"

    try:
        def sin(x): return math.sin(math.radians(x)) if angle_mode=="DEG" else math.sin(x)
        def cos(x): return math.cos(math.radians(x)) if angle_mode=="DEG" else math.cos(x)
        def tan(x): return math.tan(math.radians(x)) if angle_mode=="DEG" else math.tan(x)
        def asin(x): return math.degrees(math.asin(x)) if angle_mode=="DEG" else math.asin(x)
        def acos(x): return math.degrees(math.acos(x)) if angle_mode=="DEG" else math.acos(x)
        def atan(x): return math.degrees(math.atan(x)) if angle_mode=="DEG" else math.atan(x)

        allowed = {
            "sqrt": math.sqrt,
            "log": math.log,
            "sin": sin,
            "cos": cos,
            "tan": tan,
            "exp": math.exp,
            "factorial": math.factorial,
            "asin": asin,
            "acos": acos,
            "atan": atan,
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
            "pi": math.pi,
            "e": math.e
        }

        result = eval(expr, {"__builtins__": None}, allowed)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

        history.append(f"{expr} = {result}")
        update_history()

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Text Accissibility & Defined Fucntions #
def insert_text(text):
    functions = ["sqrt","log","sin","cos","tan","exp","factorial",
                 "asin","acos","atan","sinh","cosh","tanh"]
    if text in functions:
        entry.insert(tk.END, text + "(")
    else:
        entry.insert(tk.END, text)

def clear_entry():
    entry.delete(0, tk.END)

def clear_all():
    global memory
    entry.delete(0, tk.END)
    memory = 0

def memory_store():
    global memory
    try:
        memory = float(entry.get())
    except:
        memory = 0

def memory_recall():
    entry.insert(tk.END, str(memory))

def memory_clear():
    global memory
    memory = 0

def delete_last():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

def toggle_angle():
    global angle_mode
    angle_mode = "DEG" if angle_mode=="RAD" else "RAD"
    angle_button.config(text=angle_mode)
    status_var.set(f"Angle Mode: {angle_mode}")

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#1e1e1e" if dark_mode else "white"
    fg = "white" if dark_mode else "black"
    root.configure(bg=bg)
    entry.configure(bg=bg, fg=fg, insertbackground=fg)
    history_box.configure(bg=bg, fg=fg)
    status_bar.configure(bg=bg, fg=fg)

def update_history():
    history_box.delete(0, tk.END)
    for item in history[-20:]:
        history_box.insert(tk.END, item)

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(entry.get())

def key_input(event):
    if event.char in "0123456789.+-*/()%":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        evaluate_expression()
    elif event.keysym == "BackSpace":
        delete_last()

# Tk Window Setup #
root = tk.Tk()
root.title("Calculator")
root.geometry("900x600")

for i in range(8):
    root.grid_columnconfigure(i, weight=1)
for i in range(15):
    root.grid_rowconfigure(i, weight=1)

entry = tk.Entry(root, font=("Arial",18))
entry.grid(row=0,column=0,columnspan=8,sticky="nsew")

buttons = [
    "7","8","9","/","sqrt","log",
    "4","5","6","*","sin","cos",
    "1","2","3","-","tan","exp",
    "0",".","=","+","pi","e",
    "(",")","**","//","%","factorial",
    "asin","acos","atan","sinh","cosh","tanh"
]

row,col = 1,0
for b in buttons:
    action = lambda x=b: evaluate_expression() if x=="=" else insert_text(x)
    tk.Button(root,text=b,command=action).grid(row=row,column=col,sticky="nsew")
    col+=1
    if col>5:
        col=0
        row+=1

extra = [
    ("AC",clear_all),
    ("CE",clear_entry),
    ("M+",memory_store),
    ("MR",memory_recall),
    ("MC",memory_clear),
    ("DEL",delete_last),
    ("COPY",copy_result),
    ("THEME",toggle_theme)
]

for i,(text,cmd) in enumerate(extra):
    tk.Button(root,text=text,command=cmd).grid(row=row+i//4,column=6+(i%2),sticky="nsew")

# Buttons #
angle_button = tk.Button(root,text="RAD",command=toggle_angle)
angle_button.grid(row=row+2,column=0,sticky="nsew")

history_box = tk.Listbox(root,font=("Consolas",12))
history_box.grid(row=1,column=6,rowspan=10,columnspan=2,sticky="nsew")

status_var = tk.StringVar()
status_var.set("Angle Mode: RAD")

status_bar = tk.Label(root,textvariable=status_var,anchor="w")
status_bar.grid(row=14,column=0,columnspan=8,sticky="nsew")

root.bind("<Key>", key_input)

root.mainloop()
