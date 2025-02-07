import numpy as np
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import DrawingCanvasGUI, DrawingCanvasInterface
    from data import DataTransformation

class BasicBrush: 
    """
    Handles Canvas Events
    """
    def __init__(self, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface', mode:str = "manual"):
        self.drawing_canvas = drawing_canvas
        self.drawing_interface = drawing_interface
        self.canvas = self.drawing_canvas.canvas
        self.mode = mode
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.create_mark)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_released)
        
    def on_mouse_down(self, event):
        if self.mode == "auto":
            self.drawing_interface.reset_stroke_data()
        self.create_mark(event)

    def create_mark(self, event):
        rectangle = RectangleMark.create_canvas_mark(event.x, event.y, self.drawing_canvas, self.drawing_interface)
        RectangleMark.create_data_mark(rectangle, self.drawing_canvas, self.drawing_interface)

    def on_mouse_released(self, event):
        if self.mode == "auto":
            self.drawing_interface.enter_data()

class LineBrush:
    def __init__(self, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface', mode: str = "manual"):
        self.drawing_canvas = drawing_canvas
        self.drawing_interface = drawing_interface
        self.canvas = self.drawing_canvas._canvas
        self.mode = mode
        self.x0 = None
        self.y0 = None
        self.line = None
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_released)
        
    def on_mouse_down(self, event):
        if self.mode == "auto":
            self.drawing_interface.reset_stroke_data()
        self.x0 = event.x
        self.y0 = event.y
        self.line = LineMark.create_canvas_line(self.x0, self.y0, event.x, event.y, self.drawing_canvas, self.drawing_interface)

    def on_mouse_motion(self, event):
      self.canvas.coords(self.line, self.x0, self.y0, event.x, event.y)
        
    def on_mouse_released(self, event):
        LineMark.create_data_line(self.line, self.drawing_canvas, self.drawing_interface)
        if self.mode == "auto":
             self.drawing_interface.enter_data()

class LineMark:
    """
    Creates Line on Canvas
    """
    @staticmethod
    def create_canvas_line(x0: int, y0: int, x1: int, y1:int, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface'):
        color = drawing_interface.color_hex
        size = drawing_interface.size 
        canvas = drawing_canvas._canvas
        line = canvas.create_line(x0, y0, x1, y1, width=size, fill=color)
        return line
    
    @staticmethod
    def create_data_line(line: int, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface'):
        scalor = drawing_canvas.scalor
        canvas = drawing_canvas._canvas
        x0, y0, x1, y1 = canvas.coords(line)
        x0 = int(x0 // scalor)
        y0 = int(y0 // scalor)
        x1 = int(x1 // scalor)
        y1 = int(y1 // scalor)
        LineMark.bresenham_alg(x0,y0,x1,y1, drawing_interface)

    @staticmethod
    def bresenham_alg(x0:int, y0:int, x1:int, y1:int, drawing_interface: 'DrawingCanvasInterface'):
        width = drawing_interface.width
        height = drawing_interface.height
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        step_direction_x = 1 if x0 < x1 else -1                                
        step_direction_y = 1 if y0 < y1 else -1
        error = dx - dy
        while True:
            #print(f"(x0:{x0}, y0:{y0}), (x1:{x1}, y1:{y1})")
            if not CanvasFunctions.in_bounds(x0, y0, width, height):
                break                                                                                        
            LineMark.bresham_draw_width(x0, y0, dx, dy, drawing_interface)
            if x0 == x1 and y0 == y1:
                break
            e2 = error * 2
            if e2 > -dy:
                error -= dy
                x0 += step_direction_x
            if e2 < dx:
                error += dx
                y0 += step_direction_y
    
    @staticmethod
    def bresham_draw_width(y:int, x:int, dx, dy, drawing_interface: 'DrawingCanvasInterface'):
        images = [drawing_interface.canvas_data, drawing_interface.stroke_data]
        size = drawing_interface.size
        color = drawing_interface.color
        width = drawing_interface.width
        height = drawing_interface.height
        for s in range(size//2 + 1):
            if(dx<=dy):
                lower_x = x - s
                upper_x = x + s
                lower_y = y
                upper_y = y
            if(dy<=dx):
                lower_x = x
                upper_x = x
                lower_y = y - s
                upper_y = y + s
            for image in images:
                if CanvasFunctions.in_bounds(lower_x, lower_y, width, height):
                    DataTransformation.set_pixel_color(image, lower_x, lower_y,color)
                if CanvasFunctions.in_bounds(upper_x, upper_y, width, height):
                    DataTransformation.set_pixel_color(image, upper_x, upper_y,color)
        for image in images:
            DataTransformation.set_pixel_color(image, x, y, color)





class RectangleMark:
    """
    Creates Rectangle on Canvas
    """
    @staticmethod
    def create_canvas_mark(x: int, y: int, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface'):
        color = drawing_interface.color_hex
        size = drawing_interface.size 
        canvas = drawing_canvas._canvas
        rectangle = canvas.create_rectangle(x, y, (x + 1), (y + 1), fill= color, width= size)
        return rectangle
        
    @staticmethod
    def create_data_mark(rectangle: int, drawing_canvas: 'DrawingCanvasGUI', drawing_interface: 'DrawingCanvasInterface'):
        scalor = drawing_canvas.scalor
        canvas = drawing_canvas._canvas
        color = drawing_interface.color
        width = drawing_interface.width
        height = drawing_interface.height
        canvas_data = drawing_interface.canvas_data
        stroke_data = drawing_interface.stroke_data
        
        x1, y1, x2, y2 = canvas.bbox(rectangle)
        x1 = int(x1 // scalor)
        y1 = int(y1 // scalor)
        x2 = int(x2 // scalor)
        y2 = int(y2 // scalor)
        
        for x in range(x1, x2):
            for y in range(y1, y2):
                if (x < width and x >= 0 and y < height and y >= 0):
                    DataTransformation.set_pixel_color(canvas_data, y, x, color)
                    DataTransformation.set_pixel_color(stroke_data, y, x, color)

class CanvasFunctions:
    @staticmethod 
    def in_bounds(x,y,width, height) -> bool:
        if (x < width and x >= 0 and y < height and y >= 0):
            return True
        else:
            return False
