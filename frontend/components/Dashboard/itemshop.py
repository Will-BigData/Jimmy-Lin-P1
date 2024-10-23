import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_itemshop_interface(parent, changeScreen, rebuild, rnum):
    #clear everything
    for widget in parent.winfo_children():
        widget.destroy()
    #Sample Items
    items = DataManager.get_items()
    
    # Create a canvas
    canvas = tk.Canvas(parent)
    scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configure the scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a window in the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Pack the canvas and scrollbar
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas and scrollbar
    canvas.configure(yscrollcommand=scroll_y.set)

    # Create table headers
    tk.Label(scrollable_frame, text="Item", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Quantity", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Cost", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Order", font=("Helvetica", 12, "bold")).grid(row=0, column=3, padx=10, pady=5)

    quantity_entry = dict()
    def make_order(item_id, amount):
        amount = int(amount)
        if amount <= 0:
            return
        DataManager.create_order(int(item_id), int(amount))
        rebuild(['ORDERS'])

    
    # Create rows for each item
    for index, item in enumerate(items):
        # Item label
        tk.Label(scrollable_frame, text=item["item"]).grid(row=index + 1, column=0, padx=10, pady=5)

        # Quantity entry
        quantity_entry[index] = tk.Entry(scrollable_frame, width=5, validate="key", validatecommand=rnum)
        quantity_entry[index].insert(0,"0")
        quantity_entry[index].grid(row=index + 1, column=1, padx=10, pady=5)

        # Cost label
        tk.Label(scrollable_frame, text=f"${item['price']:.2f}").grid(row=index + 1, column=2, padx=10, pady=5)

        # Order button
        order_button = tk.Button(scrollable_frame, text="Order", command=lambda id=item["id"],i=index: make_order(id, quantity_entry[i].get()))
        order_button.grid(row=index + 1, column=3, padx=10, pady=5)

def order_item(item_name, quantity):
    """Handles the ordering process."""
    try:
        qty = int(quantity)
        if qty > 0:
            messagebox.showinfo("Order Successful", f"You have ordered {qty} of {item_name}.")
        else:
            messagebox.showerror("Invalid Quantity", "Please enter a positive number.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")