import tkinter as tk
from tkinter import ttk
from .login import create_login_frame;
from .signup import create_signup_frame;

def create_welcome_frame(root, changeScreen):
    tab_control = ttk.Notebook(root)
    login_tab = ttk.Frame(tab_control)
    signup_tab = ttk.Frame(tab_control)

    tab_control.add(login_tab, text="Login")
    tab_control.add(signup_tab, text="Signup")
    tab_control.pack(expand=1, fill='both')

    create_login_frame(login_tab, changeScreen)
    create_signup_frame(signup_tab)

    return tab_control