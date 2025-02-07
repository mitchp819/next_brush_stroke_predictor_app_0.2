import tkinter as tk
from tkinter import Menu


class MenuBar:
    def __init__(self, root:tk.Tk):
        menu_bar = Menu(root)
        root.config(menu = menu_bar)
        FileMenu(menu_bar)
        DataBaseMenu(menu_bar)
        DataSetMenu(menu_bar)
        pass

class FileMenu:
    from app.drawing_canvas import DrawingCanvasInterface
    def __init__(self, menu_bar: tk.Menu, drawing_interface: DrawingCanvasInterface):
        file_menu = Menu(menu_bar, tearoff=0)
        #TODO File Commands {New, Load, Save, Save As}
        file_menu.add_command(
            label="Save Dataset",
            command= drawing_interface.save_data
        )
        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )
        pass

class DataConfigMenu:
    def __init__(self, menu_bar:tk.Menu):
        data_config_menu = Menu(menu_bar)
        #TODO View Commands {Database Config, Dataset Editor, New Dataset, Compile Dataset}
        menu_bar.add_cascade(
            label="Data Config",
            menu=data_config_menu
        )
        pass

class WindowMenu: 
    def __init__(self, menu_bar:tk.Menu):
        window_menu = Menu(menu_bar)
        #TODO View Check Boxs 
        menu_bar.add_cascade(
            label="Window",
            menu=window_menu
        )
        pass

class DataBaseMenu:
    def __init__(self, menu_bar:tk.Menu):
        database_menu = Menu(menu_bar)
        info = "Select a Database to Generate From"
        database_menu.add_command(label= info)
        database_menu.add_separator()
        #TODO Select the Database to generate
        menu_bar.add_cascade(
            label="Database",
            menu=database_menu
        )
        pass

class DataSetMenu:
    def __init__(self, menu_bar:tk.Menu):
        dataset_menu = Menu(menu_bar)
        info = "Select one or many Datasets to save to"
        dataset_menu.add_command(label=info)
        dataset_menu.add_separator()
        #TODO Select the Dataset to save data to
        menu_bar.add_cascade(
            label="Dataset",
            menu=dataset_menu
        )
        pass