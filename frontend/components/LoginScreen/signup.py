import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_signup_frame(parent):
    label_signup_username = tk.Label(parent, text="Username:")
    label_signup_username.pack(pady=10)

    entry_signup_username = tk.Entry(parent)
    entry_signup_username.pack(pady=5)

    label_signup_email = tk.Label(parent, text="Email:")
    label_signup_email.pack(pady=10)

    entry_signup_email = tk.Entry(parent)
    entry_signup_email.pack(pady=5)

    label_signup_password = tk.Label(parent, text="Password:")
    label_signup_password.pack(pady=10)

    entry_signup_password = tk.Entry(parent, show='*')
    entry_signup_password.pack(pady=5)

    def signup():
        username = entry_signup_username.get()
        email = entry_signup_email.get()
        password = entry_signup_password.get()
        if not (username and email and password):
            return messagebox.showerror("Signup Failed", "All fields are required.")
        # Replace with your actual signup logic
        result = DataManager.signup(username, email, password)
        if result:
            messagebox.showinfo("Signup Successful", "Login through the login screen")
        else:
            messagebox.showerror("Signup Failed", "Username or email is already taken")

    button_signup = tk.Button(parent, text="Signup", command=signup)
    button_signup.pack(pady=20)