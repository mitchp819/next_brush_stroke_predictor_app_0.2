import tkinter as tk
import numpy as np
from PIL import Image, ImageTk, ImageGrab
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.value_setters import Variable
    

from drawing_app.brush import *
from data import *


WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DrawingCanvasInterface:
    """
    Stores Data for the Drawing Canvas
    functions:
        enter_data: 
    """
    def __init__(self, width: int, height: int, brush_size: 'Variable', color_value: 'Variable'):
        self.width = width
        self.height = height
        self.color = color_value.value
        self.color_hex = 'black'
        self.size = brush_size.value
        self.canvas_data = np.ones((self.height, self.width), dtype= np.uint8) * WHITE_VALUE
        self.prev_canvas_data = np.ones((self.height, self.width), dtype= np.uint8) * WHITE_VALUE
        self.stroke_data = None
        self.reset_stroke_data
        self.dataset = Dataset("canvas", "stroke")
    
    def enter_data(self):
        #print(f"Entry: {self.dataset.entry_count} \t (canvas, stroke) {self.canvas_data.shape}")
        #print(self.canvas_data)
        pil_image = Image.fromarray(self.canvas_data)
        pil_image.save("image.png")
        canvas = self.prev_canvas_data.copy()
        stroke = self.stroke_data.copy()
        self.dataset.append((canvas, stroke))
        self.prev_canvas_data = self.canvas_data.copy()
    
    def reset_stroke_data(self):
        self.stroke_data = np.full((self.height,self.width,), fill_value= STROKE_DEFAULT_VALUE, dtype=np.int8)

    def save_data(self, location:str = None, name:str = None):
        if location:
            self.location = location
        if name:
            self.name = name
        self.dataset.save("my_datamart", "name.pkl")
        print("Dataset Saved")
      
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
        self.brush = BasicBrush(self, self.interface, "auto")
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

class Color:
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



if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=700, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    canvas.brush = BasicBrush(canvas, interface, mode="auto")
    
    test_frame.pack()
    test_root.mainloop()


