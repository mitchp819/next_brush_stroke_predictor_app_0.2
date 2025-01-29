import tkinter as tk
import numpy as np
import pandas as pd
import time

WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DrawingCanvasInterface:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.color = 'black'
        self.size = 4
        pass
      
class DrawingCanvasGUI:
    """
    Configures Tkinter Drawing Canvas 
    """
    def __init__(self, container: tk.Frame, interface: DrawingCanvasInterface, scalor):
        self.interface = interface
        self.scalor = scalor
        gui_width = self.interface.width * self.scalor
        gui_height = self.interface.height * self.scalor
        self.canvas = tk.Canvas(master=container, width=gui_width, height=gui_height, bg='white')
        BindCanvasEvents(self)
        self.canvas.pack()

class BindCanvasEvents: 
    """
    Handles Canvas Events
    """
    def __init__(self, drawing_canvas: DrawingCanvasGUI,):
        self.drawing_canvas = drawing_canvas
        self.canvas = self.drawing_canvas.canvas
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.create_mark)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_released)
        
    def on_mouse_down(self, event):
        pass

    def create_mark(self, event):
        RectangleMark().create_mark(event.x, event.y, self.drawing_canvas)

    def on_mouse_released(self, event):
        pass   


class RectangleMark:
    """
    Creates Rectangle on Canvas
    """
    @staticmethod
    def create_mark(x: int, y: int, drawing_canvas: DrawingCanvasGUI):
        color = drawing_canvas.interface.color 
        size = drawing_canvas.interface.size 
        scalor = drawing_canvas.scalor
        canvas = drawing_canvas.canvas

        rectangle = canvas.create_rectangle(x, y, (x + 1), (y + 1), fill= color, width= size)
        RectangleMark.get_rectangle_cords(rectangle, scalor, canvas)
        
    @staticmethod
    def get_rectangle_cords(rectangle, scalor: int, canvas: tk.Canvas):
        x1, y1, x2, y2 = canvas.bbox(rectangle)
        x1 = int(x1 // scalor)
        y1 = int(y1 // scalor)
        x2 = int(x2 // scalor)
        y2 = int(y2 // scalor)
        







if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=400, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 2)
    
    test_frame.pack()
    test_root.mainloop()


