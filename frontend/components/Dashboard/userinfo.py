import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_user_info_frame(parent, changeScreen, rebuild, rnum):
    #clear everything
    for widget in parent.winfo_children():
        widget.destroy()

    # Create a new frame
    user_info_frame = tk.Frame(parent)
    user_info_frame.pack(pady=10, padx=10)

    # Fetch user data
    user = DataManager.get_user() or {}
    username = user.get('username', 'N/A')  # Default to 'N/A' if not found
    email = user.get('email', 'N/A')        # Default to 'N/A' if not found
    funds = user.get('funds', 0)            # Default to 0 if not found

    # Font settings
    label_font = ("Arial", 12)  # Font for labels
    button_font = ("Arial", 12)  # Font for buttons

    # Username Label
    label_username = tk.Label(user_info_frame, text="Username: ", font=label_font)
    label_username.grid(row=0, column=0, sticky=tk.W)

    username_value = tk.Label(user_info_frame, text=username, font=label_font)
    username_value.grid(row=0, column=1, sticky=tk.W)

    # Email Label
    label_email = tk.Label(user_info_frame, text="Email: ", font=label_font)
    label_email.grid(row=1, column=0, sticky=tk.W)

    email_value = tk.Label(user_info_frame, text=email, font=label_font)
    email_value.grid(row=1, column=1, sticky=tk.W)

    # Funds Label
    label_funds = tk.Label(user_info_frame, text="Funds: ", font=label_font)
    label_funds.grid(row=2, column=0, sticky=tk.W)

    funds_value = tk.Label(user_info_frame, text=f"{funds}G", font=label_font)
    funds_value.grid(row=2, column=1, sticky=tk.W)

    # Add Funds Section
    add_funds_label = tk.Label(user_info_frame, text="Add Funds:", font=label_font)
    add_funds_label.grid(row=3, column=0, sticky=tk.W)

    funds_entry = tk.Entry(user_info_frame, width=10, font=button_font, validate="key", validatecommand=rnum)
    funds_entry.grid(row=3, column=1, sticky=tk.W)

    # Function to handle adding funds
    def add_funds():
        try:
            amount = int(funds_entry.get())
            updated = DataManager.update_funds(amount)
            funds_value.config(text=f"${updated:.2f}")
            funds_entry.delete(0, tk.END)  
        except ValueError as e:
            messagebox.showerror("Error", "Must be an integer")

    # Add Funds Button
    add_funds_button = tk.Button(user_info_frame, text="Add Funds", command=add_funds, font=button_font)
    add_funds_button.grid(row=4, column=0, pady=(10, 5))  # Add vertical padding (10, 5)

    # Logout Function
    def logout():
        DataManager.logout()
        changeScreen("WELCOME")  # Change to the welcome screen or login screen

    # Logout Button
    logout_button = tk.Button(user_info_frame, text="Logout", command=logout, font=button_font)
    logout_button.grid(row=4, column=1, pady=(10, 5))  # Add vertical padding (10, 5)

    return user_info_frame