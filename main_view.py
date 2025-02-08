import tkinter as tk
from data import Dataset
from app import DrawingCanvasGUI
from ds_viewer import ViewerInterface

if __name__ == "__main__":
    dataset = Dataset()
    dataset.load("dataset\\name.pkl")
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
    viewer_interface = ViewerInterface(dataset)
    drawing_canvas = DrawingCanvasGUI(test_frame, ViewerInterface)

    test_frame.pack()
    test_root.mainloop()
    pass
else: 
    pass