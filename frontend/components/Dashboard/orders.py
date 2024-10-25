import tkinter as tk
from tkinter import messagebox
from api.DataManager import DataManager

def create_orders_interface(parent, changeScreen, rebuild, rnum):
    # Clear everything
    for widget in parent.winfo_children():
        widget.destroy()
    
    # Sample orders
    orders = DataManager.get_orders()

    # Calculate total cost of committed items
    total_committed_cost = sum(item["amount"] * item["price"] for item in orders if not item["commited"])
    total_frame = tk.Frame(parent)
    total_frame.pack(pady=10)

    # Display total committed cost above the table
    total_label = tk.Label(total_frame, text="Total:", font=("Helvetica", 14, "bold"))
    total_label.grid(row=0, column=0, padx=(0, 10))  # Move to the left

    total_cost_display = tk.Label(total_frame, text=f"${total_committed_cost:.2f}", font=("Helvetica", 14))
    total_cost_display.grid(row=0, column=1)  # Total cost display

    def commit():
        if not total_committed_cost:
            return
        result = DataManager.commit_order()
        if result:
            create_orders_interface(parent, changeScreen, rebuild, rnum)
            rebuild(('INVENTORY','USER'))
        else:
            messagebox.showerror("Commit Failed", "Insufficient Funds")
        

    # Add Commit button
    commit_button = tk.Button(total_frame, text="Commit", command=commit)
    commit_button.grid(row=0, column=2, padx=(10, 0))  # Position on the right
    
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
    tk.Label(scrollable_frame, text="Amount", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
    tk.Label(scrollable_frame, text="Actions", font=("Helvetica", 12, "bold")).grid(row=0, column=3, columnspan=2, padx=10, pady=5)

    # Create rows for each item
    for index, item in enumerate(orders):
        # Calculate total cost
        total_cost = item["amount"] * item["price"]
        
        # Item label
        tk.Label(scrollable_frame, text=item["item"]).grid(row=index + 1, column=0, padx=10, pady=5)

        # Total cost label
        tk.Label(scrollable_frame, text=f"{total_cost}G").grid(row=index + 1, column=1, padx=10, pady=5)
        # Amount entry or label
        if not item["commited"]:
            # Editable amount entry
            amount_entry = tk.Entry(scrollable_frame, width=5, validate="key", validatecommand=rnum)
            amount_entry.insert(0, str(item["amount"]))
            amount_entry.grid(row=index + 1, column=2, padx=10, pady=5)

            # Update button
            update_button = tk.Button(
                scrollable_frame, text="Update",
                command=lambda item=item, entry=amount_entry: update_item(item["id"], entry.get())
            )
            update_button.grid(row=index + 1, column=3, padx=5, pady=5)

            # Delete button
            delete_button = tk.Button(
                scrollable_frame, text="Delete",
                command=lambda item=item: delete_item(item["id"])
            )
            delete_button.grid(row=index + 1, column=4, padx=5, pady=5)
        else:
            # Display amount as a label if committed
            tk.Label(scrollable_frame, text=str(item["amount"])).grid(row=index + 1, column=2, padx=10, pady=5)
            tk.Label(scrollable_frame, text="Completed", fg="green").grid(row=index + 1, column=3, padx=5, pady=5)


    def update_item(id, amount):
        amount = int(amount)
        if amount <= 0:
            return
        DataManager.update_order(id, amount)
        create_orders_interface(parent, changeScreen, rebuild, rnum)

    def delete_item(id):
        DataManager.delete_order(id)
        create_orders_interface(parent, changeScreen, rebuild, rnum)