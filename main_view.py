import tkinter as tk
from data import Dataset
from app import DrawingCanvasGUI
from ds_viewer import EntryView

if __name__ == "__main__":
    dataset = Dataset()
    dataset.load(r"my_datamart\name.pkl")
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root, bg = '#52DA46')
    EntryView(test_frame, dataset)

    test_frame.pack()
    test_root.mainloop()
