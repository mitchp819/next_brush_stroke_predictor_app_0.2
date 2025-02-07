import tkinter as tk
from app import *

if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=700, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    canvas.brush = BasicBrush(canvas, interface, mode="auto")
    MenuBar(test_root)
    
    test_frame.pack()
    test_root.mainloop()