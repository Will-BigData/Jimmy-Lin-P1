from tkinter import ttk
from .itemshop import create_itemshop_interface
from .userinfo import create_user_info_frame
from .orders import create_orders_interface
from .inventory import create_inventory_interface



def create_dashboard_frame(root, changeScreen):
    tab_control = ttk.Notebook(root)
    item_shop = ttk.Frame(tab_control)
    orders = ttk.Frame(tab_control)
    user_info = ttk.Frame(tab_control)
    inventory = ttk.Frame(tab_control)

        # Validation function to allow only numbers
    def validate_number(input_value):
        if input_value == "" or input_value == "0":
                return True
        # Return True only if the input is numeric
        return input_value.isdigit()

    rnum = (root.register(validate_number), '0')

    tab_control.add(item_shop, text="Item Shop")
    tab_control.add(orders, text="Orders")
    tab_control.add(inventory, text="Inventory")
    tab_control.add(user_info, text="User")
    tab_control.pack(expand=1, fill='both')

    def rebuild(tabs=['ITEMSHOP', 'USER', 'ORDERS', 'INVENTORY']):
        if 'ITEMSHOP' in tabs:
            create_itemshop_interface(item_shop, changeScreen, rebuild, rnum)
        if 'USER' in tabs:
            create_user_info_frame(user_info, changeScreen, rebuild, rnum)
        if 'ORDERS' in tabs:
            create_orders_interface(orders, changeScreen, rebuild, rnum)
        if 'INVENTORY' in tabs:
            create_inventory_interface(inventory, changeScreen, rebuild, rnum)
    
    rebuild()
    return tab_control