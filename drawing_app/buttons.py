import tkinter as tk

BASE_BUTTON_COLOR = "blue"

class BaseButton(tk.Button):
    def __init__(self, master):
        self.config(
            bg = BASE_BUTTON_COLOR,
            relief="raised",
            master = master
        )
    pass

class SaveButton:
    pass