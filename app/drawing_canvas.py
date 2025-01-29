import tkinter as tk
import numpy as np
import pandas as pd
import time

from brush import *

WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DrawingCanvasInterface:
    """
    Stores Data for the Drawing Canvas
    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.color = 0
        self.color_hex = 'black'
        self.size = 4
        self.canvas_data = np.ones((width, height), dtype= np.uint8) * WHITE_VALUE
        self.stroke_data = np.full((width, height), fill_value= STROKE_DEFAULT_VALUE, dtype=np.int8)
        pass
      
class DrawingCanvasGUI:
    """
    Configures Tkinter Drawing Canvas 
    """
    def __init__(self, container: tk.Frame, interface: DrawingCanvasInterface, scalor):
        self.interface = interface
        self._scalor = scalor
        self.gui_width = self.interface.width * self.scalor
        self.gui_height = self.interface.height * self.scalor
        self.canvas = tk.Canvas(master=container, width=self.gui_width, height=self.gui_height, bg='white')
        BasicBrush(self)
        self.canvas.pack()
    
    @property
    def scalor(self):
        return self._scalor
    
    @scalor.setter
    def set_scalor(self, value):
        self._scalor = value
        self.gui_width = self.interface.width * self._scalor
        self.gui_height = self.interface.height * self._scalor
        self.canvas.config(width = self.gui_width, height = self.gui_height)
        pass

    def load_np_image(self, image: np):
        if image.shape != (self.gui_width, self.gui_height):
            self.scale_np_image_to_canvas(image)
            pass
        for row, column_array in enumerate(image):
            for col, pixel_value in enumerate(column_array):
                hex_color = Color.greyscale_value_to_hex(pixel_value)
                self.canvas.create_rectangle(
                    col, row, (col+1),
                    (row+1), fill=hex_color)
        pass

    def scale_np_image_to_canvas(self, image: np):
        pass

class Color():
    def hex_to_greyscale_value(hex_color: str):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        grayscale_value = round((r + g + b) / 3)
        return grayscale_value
    
    def greyscale_value_to_hex(value):
        return f"#{value:02x}{value:02x}{value:02x}"






if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=400, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    
    test_frame.pack()
    test_root.mainloop()


