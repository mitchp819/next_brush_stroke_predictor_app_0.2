import tkinter as tk
import numpy as np
import pandas as pd
from PIL import Image, ImageTk, ImageGrab
import time

from brush import *
from dataset import Dataset
from data_transform import DataTransformation

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
        self.size = 1
        self.canvas_data = np.ones((self.height, self.width), dtype= np.uint8) * WHITE_VALUE
        self.stroke_data = None
        self.reset_stroke_data
        self.dataset = Dataset("canvas", "stroke")
    
    def enter_data(self):
        #print(f"Entry: {self.dataset.entry_count} \t (canvas, stroke) {self.canvas_data.shape}")
        #print(self.canvas_data)
        pil_image = Image.fromarray(self.canvas_data)
        pil_image.save("image.png")
        self.dataset.append((self.canvas_data, self.stroke_data))
    
    def reset_stroke_data(self):
        self.stroke_data = np.full((self.height,self.width,), fill_value= STROKE_DEFAULT_VALUE, dtype=np.int8)
      
class DrawingCanvasGUI:
    """
    Configures Tkinter Drawing Canvas 
    """
    def __init__(self, container: tk.Frame, interface: DrawingCanvasInterface, scalor):
        self.interface = interface
        self._scalor = scalor
        self.gui_width = self.interface.width * self.scalor
        self.gui_height = self.interface.height * self.scalor
        self._canvas = tk.Canvas(master=container, width=self.gui_width, height=self.gui_height, bg='white')
        self.brush = BasicBrush(self, self.interface)
        self._canvas.pack()
    
    @property
    def scalor(self):
        return self._scalor
    
    @scalor.setter
    def set_scalor(self, value):
        self._scalor = value
        self.gui_width = self.interface.width * self._scalor
        self.gui_height = self.interface.height * self._scalor
        canvas = self.get_pil_image()
        self._canvas.config(width = self.gui_width, height = self.gui_height)
        self.load_pil_image(canvas)
        pass

    @property
    def canvas(self):
        return self._canvas
    
    @canvas.setter
    def set_canvas(self, image):
        if isinstance(image, Image):
            self.load_pil_image(image)
            return
        if isinstance(image, np):
            self.load_np_image(image)
            return
        raise ValueError("image must be a PIL Image or a Numpy Array")

    def get_pil_image(self) -> Image:
        x = self._canvas.winfo_rootx()
        y = self._canvas.winfo_rooty()
        x1 = x + self._canvas.winfo_width()
        y1 = y + self._canvas.winfo_height()
        image = ImageGrab.grab().crop((x, y, x1, y1))
        return image

    def load_np_image(self, image: np) -> None:
        if image.shape != (self.gui_width, self.gui_height):
            image = DataTransformation.transform_np_image(image, self.gui_width, self.gui_height)
        for row, column_array in enumerate(image):
            for col, pixel_value in enumerate(column_array):
                hex_color = Color.greyscale_value_to_hex(pixel_value)
                self._canvas.create_rectangle(
                    col, row, (col+1),
                    (row+1), fill=hex_color)
        pass

    def load_pil_image(self, image:Image):
        image = image.resize((self.gui_width, self.gui_height), Image.NEAREST)
        photo = ImageTk.PhotoImage(image)
        self._canvas.create_image(0,0, anchor = 'NW', image=photo)
        canvas.image = photo
        pass
    

class DataTransformation:
    @staticmethod
    def scale_np_image(image: np, scale):
        pass
    
    @staticmethod
    def transform_np_image(image: np, new_width: int, new_height: int) -> np:
        """
        Transforms a np.array image to a new width and height
        """
        pil_image = Image.fromarray(image)
        resized_image = pil_image.resize(
            (new_width, new_height),
            resample = Image.NEAREST)
        resized_np = np.array(resized_image)
        return resized_np

class Color():
    @staticmethod
    def hex_to_greyscale_value(hex_color: str):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        grayscale_value = round((r + g + b) / 3)
        return grayscale_value
    
    @staticmethod
    def greyscale_value_to_hex(value):
        return f"#{value:02x}{value:02x}{value:02x}"




class TestButton:
    def __init__(self, master, interface, canvas):
        self.interface = interface
        self.canvas = canvas
        btn = tk.Button(
            master, 
            text= "test button does something",
            command = self.on_button_click)
        btn.pack()
        pass

    def on_button_click(self):
        print("test button doing something")
        pass

if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=700, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    canvas.brush = LineBrush(canvas, interface, mode="auto")
    TestButton(test_root, interface, canvas)
    
    test_frame.pack()
    test_root.mainloop()


