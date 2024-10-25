import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_item_entry_frame(parent, changeScreen, rebuild, rnum):
    # Clear everything
    for widget in parent.winfo_children():
        widget.destroy()
    
    # Sample Items
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
    tk.Label(scrollable_frame, text="Price", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Actions", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)

    # Store entries for each item price for updates
    price_entry = dict()

    # Function to handle updating an item price
    def update_price(item_id, item):
        print("ran")
        try:
            DataManager.update_item(item_id, item)
            rebuild(['ITEMSHOP','ADMIN_ITEMS'])  # Refresh the page after deletion
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number.")


    # Function to handle deleting an item
    def delete_item(item_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?"):
            DataManager.delete_item(item_id)
            rebuild(['ITEMSHOP','ADMIN_ITEMS'])  # Refresh the page after deletion

    # Create rows for each item
    for index, item in enumerate(items):
        # Item label
        tk.Label(scrollable_frame, text=item["item"]).grid(row=index + 1, column=0, padx=10, pady=5)

        # Price entry
        price_entry[index] = tk.Entry(scrollable_frame, width=10, validate="key", validatecommand=rnum)
        price_entry[index].insert(0, f"{item['price']}")
        price_entry[index].grid(row=index + 1, column=1, padx=10, pady=5)

        # Actions: Update and Delete buttons
        action_frame = tk.Frame(scrollable_frame)
        action_frame.grid(row=index + 1, column=2, padx=10, pady=5)

        # Update Button
        update_button = tk.Button(action_frame, text="Update", command=lambda id=item["id"], itemn=item['item'], cost=price_entry[index].get(): update_price(id, {"item":itemn, "price":cost}))
        update_button.pack(side=tk.LEFT, padx=5)

        # Delete Button
        delete_button = tk.Button(action_frame, text="Delete", command=lambda id=item["id"]: delete_item(id))
        delete_button.pack(side=tk.LEFT, padx=5)

    return scrollable_frame