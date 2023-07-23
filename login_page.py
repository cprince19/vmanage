import tkinter as tk
from tkinter import messagebox

# Dummy user credentials for demonstration purposes
dummy_username = "user123"
dummy_password = "password123"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == dummy_username and password == dummy_password:
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def create_login_page():
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("300x150")

    label_username = tk.Label(root, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    btn_login = tk.Button(root, text="Login", command=login)
    btn_login.pack()

    root.mainloop()

if __name__ == "__main__":
    create_login_page()
