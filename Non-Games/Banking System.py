# Imports #
from tkinter import *
import json

# Tk Window Setup #
root = Tk()
root.title("Banking System")
root.geometry("400x200")

Label(root, text="Welcome to The Bank, but this time in python").pack()
Label(root, text="Choose an option").pack()

# ================= ACCOUNT CLASS ================= #
class Account:
    def __init__(self, firstname, lastname, password, balance=0):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Increase balance #

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Decrease balance #
            return True
        return False

    def to_dict(self):
        return self.__dict__  # Convert object to dict #

# ================= FILE FUNCTIONS ================= #
def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)

# ================= CREATE ACCOUNT ================= #
def create_acc():
    win = Toplevel(root)
    win.title("Create Account")

    Label(win, text="First Name").pack()
    f = Entry(win); f.pack()

    Label(win, text="Last Name").pack()
    l = Entry(win); l.pack()

    Label(win, text="Password").pack()
    p = Entry(win, show="*"); p.pack()

    def submit():
        acc = Account(f.get(), l.get(), p.get())
        data = load_accounts()
        data.append(acc.to_dict())
        save_accounts(data)
        Label(win, text="Account Created!").pack()

    Button(win, text="Create", command=submit).pack()

# ================= DASHBOARD ================= #
def open_dashboard(user, index):
    dash = Toplevel(root)
    dash.title("Dashboard")
    dash.geometry("300x250")

    def refresh_label():
        balance_label.config(text=f"Balance: {user['balance']}")

    balance_label = Label(dash, text=f"Balance: {user['balance']}")
    balance_label.pack()

    # -------- Deposit -------- #
    def deposit():
        try:
            amt = int(amount_entry.get())
        except ValueError:
            Label(dash, text = "Enter a valid number").pack
            return

        user["balance"] += amt  # Add money #
        data = load_accounts()
        data[index] = user
        save_accounts(data)
        refresh_label()

    # -------- Withdraw -------- #
    def withdraw():
        amt = int(amount_entry.get())
        if amt <= user["balance"]:
            user["balance"] -= amt  # Remove money #
            data = load_accounts()
            data[index] = user
            save_accounts(data)
            refresh_label()
        else:
            Label(dash, text="Insufficient Balance").pack()

    Label(dash, text="Amount").pack()
    amount_entry = Entry(dash)
    amount_entry.pack()

    Button(dash, text="Deposit", command=deposit).pack(pady=5)
    Button(dash, text="Withdraw", command=withdraw).pack(pady=5)

    # -------- Check Balance -------- #
    def check_balance():
        refresh_label()  # Update display #

    Button(dash, text="Check Balance", command=check_balance).pack(pady=5)

    # -------- Logout -------- #
    def logout():
        dash.destroy()  # Close dashboard #

    Button(dash, text="Logout", command=logout).pack(pady=10)

# ================= LOGIN ================= #
def access_acc():
    win = Toplevel(root)
    win.title("Login")

    Label(win, text="First Name").pack()
    f = Entry(win); f.pack()

    Label(win, text="Password").pack()
    p = Entry(win, show="*"); p.pack()

    def login():
        data = load_accounts()
        for i, acc in enumerate(data):
            if acc["firstname"] == f.get() and acc["password"] == p.get():
                open_dashboard(acc, i)
                return
        Label(win, text="Invalid Login").pack()

    Button(win, text="Login", command=login).pack()

# ================= MAIN BUTTONS ================= #
Button(root, text="Create Account", command=create_acc).pack(pady=5)
Button(root, text="Access Account", command=access_acc).pack(pady=5)

root.mainloop()
