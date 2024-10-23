import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_inventory_interface(parent, changeScreen, rebuild, rnum):
    # Clear everything
    for widget in parent.winfo_children():
        widget.destroy()

    # Sample Inventory Items
    items = DataManager.get_inventory()  # Assuming this method retrieves inventory items
    print(items)

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
    tk.Label(scrollable_frame, text="Update", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)

    quantity_entry = dict()

    def update_inventory(item_id, amount):
        amount = int(amount)
        if amount < 0:
            messagebox.showerror("Invalid Quantity", "Quantity cannot be negative.")
            return
        # DataManager.update_inventory_item(item_id, amount)  # Assuming this method updates inventory
        rebuild(['INVENTORY'])

    # Create rows for each inventory item
    for index, item in enumerate(items):
        # Item label
        tk.Label(scrollable_frame, text=item["item"]).grid(row=index + 1, column=0, padx=10, pady=5)

        # Quantity label
        tk.Label(scrollable_frame, text=item["quantity"]).grid(row=index + 1, column=1, padx=10, pady=5)

        # Quantity entry for updating
        quantity_entry[index] = tk.Entry(scrollable_frame, width=5, validate="key")
        quantity_entry[index].insert(0, "0")
        quantity_entry[index].grid(row=index + 1, column=2, padx=10, pady=5)

        # Update button
        update_button = tk.Button(scrollable_frame, text="Update", command=lambda id=item["id"], i=index: update_inventory(id, quantity_entry[i].get()))
        update_button.grid(row=index + 1, column=3, padx=10, pady=5)

    # Back button to change screens
    back_button = tk.Button(scrollable_frame, text="Back", command=changeScreen)
    back_button.grid(row=len(items) + 1, column=0, columnspan=4, pady=10)