import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_login_frame(parent, changeScreen):
    label_login_email = tk.Label(parent, text="Email:")
    label_login_email.pack(pady=10)

    entry_login_email = tk.Entry(parent)
    entry_login_email.pack(pady=5)

    label_login_password = tk.Label(parent, text="Password:")
    label_login_password.pack(pady=10)

    entry_login_password = tk.Entry(parent, show='*')
    entry_login_password.pack(pady=5)

    def login():
        email = entry_login_email.get()
        password = entry_login_password.get()
        
        # Replace with your actual authentication logic
        result = DataManager.login(email, password)
        if result:
            changeScreen("DASHBOARD")
        else:
            print("failed")
        
        # show_main_app()

    button_login = tk.Button(parent, text="Login", command=login)
    button_login.pack(pady=20)