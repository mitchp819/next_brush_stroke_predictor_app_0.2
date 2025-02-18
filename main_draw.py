import tkinter as tk
from drawing_app import DrawingCanvasGUI, DrawingCanvasInterface, BasicBrush, MenuBar, LineBrush
from ui import Variable, ValueSetterPack

if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)

    brush_size = Variable(10, 0, 50)
    color_value = Variable(0, 0, 255)

    brush_setter = ValueSetterPack(test_frame, brush_size)
   
    interface = DrawingCanvasInterface(width=700, height=400, brush_size=brush_size, color_value=color_value)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    #canvas.brush = LineBrush(canvas, interface, "auto")
    MenuBar(test_root, interface)
    
    test_frame.pack()
    test_root.mainloop()