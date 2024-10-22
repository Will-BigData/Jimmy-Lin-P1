import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_orders_interface(parent, changeScreen, rebuild, rnum):
    # Clear everything
    for widget in parent.winfo_children():
        widget.destroy()
    
    # Sample orders
    orders = DataManager.get_orders()
    print(orders)
    
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
    tk.Label(scrollable_frame, text="Total Cost", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Amount", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Actions", font=("Helvetica", 12, "bold")).grid(row=0, column=3, columnspan=2, padx=10, pady=5)

    # Create rows for each item
    for index, item in enumerate(orders):
        # Calculate total cost
        total_cost = item["amount"] * item["price"]
        
        # Item label
        tk.Label(scrollable_frame, text=item["item"]).grid(row=index + 1, column=0, padx=10, pady=5)

        # Total cost label
        tk.Label(scrollable_frame, text=f"${total_cost:.2f}").grid(row=index + 1, column=1, padx=10, pady=5)

        # Amount entry or label
        if not item["commited"]:
            # Editable amount entry
            amount_entry = tk.Entry(scrollable_frame, width=5, validate="key", validatecommand=rnum)
            amount_entry.insert(0, str(item["amount"]))
            amount_entry.grid(row=index + 1, column=2, padx=10, pady=5)

            # Update button
            update_button = tk.Button(
                scrollable_frame, text="Update",
                command=lambda item=item, entry=amount_entry: update_item(item["item"], entry.get())
            )
            update_button.grid(row=index + 1, column=3, padx=5, pady=5)

            # Delete button
            delete_button = tk.Button(
                scrollable_frame, text="Delete",
                command=lambda item=item: delete_item(item["item"])
            )
            delete_button.grid(row=index + 1, column=4, padx=5, pady=5)
        else:
            # Display amount as a label if committed
            tk.Label(scrollable_frame, text=str(item["amount"])).grid(row=index + 1, column=2, padx=10, pady=5)

    def update_item(item_name, new_amount):
        """Handles the updating process for the item's amount."""
        try:
            qty = int(new_amount)
            if qty >= 0:
                messagebox.showinfo("Update Successful", f"The amount for {item_name} has been updated to {qty}.")
                # You might add code here to update the data source or API.
            else:
                messagebox.showerror("Invalid Quantity", "Please enter a non-negative number.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def delete_item(item_name):
        """Handles the deletion process for the item."""
        response = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {item_name}?")
        if response:
            messagebox.showinfo("Deletion Successful", f"{item_name} has been deleted.")
            # You might add code here to remove the item from the data source or API.