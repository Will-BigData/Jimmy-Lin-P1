import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_item_entry_frame(parent, changeScreen, rnum):
    # Clear everything
    for widget in parent.winfo_children():
        widget.destroy()

    # Create a new frame
    item_entry_frame = tk.Frame(parent)
    item_entry_frame.pack(pady=10, padx=10)

    # Font settings
    label_font = ("Arial", 12)  # Font for labels
    button_font = ("Arial", 12)  # Font for buttons

    # Item Name Label
    label_item_name = tk.Label(item_entry_frame, text="Item Name: ", font=label_font)
    label_item_name.grid(row=0, column=0, sticky=tk.W)

    item_name_entry = tk.Entry(item_entry_frame, width=20, font=button_font)
    item_name_entry.grid(row=0, column=1, sticky=tk.W)

    # Item Price Label
    label_price = tk.Label(item_entry_frame, text="Price: ", font=label_font)
    label_price.grid(row=1, column=0, sticky=tk.W)

    price_entry = tk.Entry(item_entry_frame, width=10, font=button_font, validate="key", validatecommand=rnum)
    price_entry.grid(row=1, column=1, sticky=tk.W)

    # Function to handle item submission
    def submit_item():
        item_name = item_name_entry.get()
        try:
            price = float(price_entry.get())
            DataManager.add_item(item_name, price)  # Assuming add_item is a method in DataManager
            messagebox.showinfo("Success", f"Item '{item_name}' with price {price} added successfully!")
            item_name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")

    # Submit Button
    submit_button = tk.Button(item_entry_frame, text="Submit", command=submit_item, font=button_font)
    submit_button.grid(row=2, column=0, columnspan=2, pady=(10, 5))  # Center the button and add padding

    return item_entry_frame