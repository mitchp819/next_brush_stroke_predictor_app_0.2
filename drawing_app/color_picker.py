import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk, ImageGrab

from drawing_app.drawing_canvas import Color

WHITE_VALUE = 255

class GreyScalePicker:
    def __init__(self, container:tk.Frame, width:int = 30, default:int = 0):
        main_frame = tk.Frame(container).pack()
        self.value_entry = ttk.Entry(
            main_frame,
            textvariable=default
        ).pack(side="left")
        canvas =GreyScalePicker.greyscale_gradient_canvas(main_frame, width)
        canvas.pack(side='left')

    @property
    def value(self):
        return self._value
    
    @value.setter
    def set_value(self, value):
        self._value.set(value)

        

    @staticmethod
    def greyscale_gradient_canvas(container, height):
        canvas = tk.Canvas(
            master=container,
            width=WHITE_VALUE, 
            height=height)
        for color_value in range(WHITE_VALUE):
            color_hex = Color.greyscale_value_to_hex(color_value)
            canvas.create_line(
                color_value,0,
                color_value,height, 
                width=1, 
                fill=color_hex)
        return canvas




