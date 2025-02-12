import tkinter as tk
from drawing_app import DrawingCanvasGUI, DrawingCanvasInterface, BasicBrush, MenuBar

if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
   
    interface = DrawingCanvasInterface(width=700, height=400)
    canvas = DrawingCanvasGUI(test_frame, interface, 1)
    canvas.brush = BasicBrush(canvas, interface, mode="auto")
    MenuBar(test_root, interface)
    
    test_frame.pack()
    test_root.mainloop()