from tkinter import ttk
from .itemshop import create_itemshop_interface
from .userinfo import create_user_info_frame

def create_dashboard_frame(root, changeScreen):
    tab_control = ttk.Notebook(root)
    item_shop = ttk.Frame(tab_control)
    user_info = ttk.Frame(tab_control)

    tab_control.add(item_shop, text="Item Shop")
    tab_control.add(user_info, text="User")
    tab_control.pack(expand=1, fill='both')

    create_itemshop_interface(item_shop, changeScreen)
    create_user_info_frame(user_info, changeScreen)

    return tab_control