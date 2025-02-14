import tkinter as tk
from tkinter import Menu
from typing import TYPE_CHECKING

class MenuBar:
    def __init__(self, root:tk.Tk):
        menu_bar = Menu(root)
        root.config(menu = menu_bar)
    pass

class FileMenu:
    def __init__(self, menu_bar: tk.Menu):
        file_menu = Menu(menu_bar, tearoff=0)
        #TODO File Commands {New, Load, Save, Save As}
        file_menu.add_command(
            label="Load Dataset",
            # command=
        )
        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )
        pass