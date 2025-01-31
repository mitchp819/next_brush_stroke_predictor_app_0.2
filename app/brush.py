from drawing_canvas import DrawingCanvasGUI

class BasicBrush: 
    """
    Handles Canvas Events
    """
    def __init__(self, drawing_canvas: DrawingCanvasGUI,):
        self.drawing_canvas = drawing_canvas
        self.canvas = self.drawing_canvas._canvas
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.create_mark)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_released)
        
    def on_mouse_down(self, event):
        self.create_mark(event)
        pass

    def create_mark(self, event):
        rectangle = RectangleMark.create_canvas_mark(event.x, event.y, self.drawing_canvas)
        RectangleMark.create_data_mark(rectangle, self.drawing_canvas)

    def on_mouse_released(self, event):
        pass   


class RectangleMark:
    """
    Creates Rectangle on Canvas
    """
    @staticmethod
    def create_canvas_mark(x: int, y: int, drawing_canvas: DrawingCanvasGUI):
        color = drawing_canvas.interface.color_hex
        size = drawing_canvas.interface.size 
        canvas = drawing_canvas._canvas

        rectangle = canvas.create_rectangle(x, y, (x + 1), (y + 1), fill= color, width= size)
        return rectangle
        
    @staticmethod
    def create_data_mark(rectangle: int, drawing_canvas: DrawingCanvasGUI):
        scalor = drawing_canvas.scalor
        canvas = drawing_canvas._canvas
        color = drawing_canvas.interface.color
        width = drawing_canvas.interface.width
        height = drawing_canvas.interface.height
        canvas_data = drawing_canvas.interface.canvas_data
        stroke_data = drawing_canvas.interface.stroke_data
        
        x1, y1, x2, y2 = canvas.bbox(rectangle)
        x1 = int(x1 // scalor)
        y1 = int(y1 // scalor)
        x2 = int(x2 // scalor)
        y2 = int(y2 // scalor)
        
        for x in range(x1, x2):
            for y in range(y1, y2):
                if (x < width and x >= 0 and y < height and y >= 0):
                    canvas_data[y, x] = color
                    stroke_data[y, x] = color