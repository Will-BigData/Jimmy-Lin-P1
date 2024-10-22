import tkinter as tk
from tkinter import ttk
from .LoginScreen.welcome import create_welcome_frame
from .Dashboard.dashboard import create_dashboard_frame

class ScreenManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login / Signup")
        self.root.geometry("400x300")
        self.screen = 'LOGIN'
        self.frames = {
            "WELCOME": lambda: create_welcome_frame(self.root, changeScreen=self.show_frame),
            "DASHBOARD": lambda: create_dashboard_frame(self.root, changeScreen=self.show_frame)
        }
        self.show_frame("WELCOME")
    
    def run(self):
        self.root.mainloop()

    def show_frame(self, screen):
        """ Display the specified frame. """
        # Clear the current frame
        self.clear_frame()

        # Generate and show the requested frame
        if screen in self.frames:
            frame = self.frames[screen]()  # Call the lambda to create the frame
            frame.pack(fill=tk.BOTH, expand=True)
        else:
            print(f"Screen '{screen}' not found.")

    def clear_frame(self):
        """ Clear the current frame. """
        for widget in self.root.winfo_children():
            widget.destroy()  # Remove all widgets from the root window