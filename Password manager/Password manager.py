import tkinter as tk
from tkinter import messagebox


def on_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Login Failed", "Please enter both username and password.")
        return

    # Replace this check with your real authentication logic
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Success", "Welcome, {}!".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")



