import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from data import DatasetValidation as dv, DataTransformation as dt
from ui import ScrollContainer

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data import Dataset


class EntryView:
    
    def __init__(self,container: tk, dataset:'Dataset'):
        main_frame = tk.Frame(container, bg = '#A822B2')
        main_frame.pack(fill="x", padx=5, pady=5)
        scroll_frame = ScrollContainer.create_scrollbar(main_frame,1200,700)
        entry_frame = tk.Frame(scroll_frame, bg ='red')
        entry_frame.pack()
        self.create_entrys(entry_frame, dataset)
        
        
    @staticmethod
    def create_entrys( container:tk, cs_dataset:'Dataset'):
        #Does this need to be faster? 
        ds = cs_dataset.dataset
        row_count = cs_dataset.entry_count
        canvas_entrys = ds["canvas"]
        stroke_entrys = ds["stroke"]
        for row in range(0,row_count):
            holder_frame = tk.Frame(container)
            holder_frame.pack()
            lbl = tk.Label(holder_frame, text=f"Entry: {row}", bg= '#94EBA4')
            lbl.pack()
            canvas = dt.np_image_to_tk(canvas_entrys[row], new_width= 400)
            stroke = dt.np_image_to_tk(stroke_entrys[row], new_width= 400)
            EntryView.entry_row(holder_frame, canvas, stroke, "(100x100)", "1:1")

    @staticmethod
    def entry_row( container:tk.Widget, canvas:tk.PhotoImage, stroke:tk.PhotoImage, size:str =None, ratio:str = None):
        entry_frame = tk.Frame(container)
        entry_frame.columnconfigure(0, weight = 3)
        entry_frame.columnconfigure(1, weight = 3)
        entry_frame.columnconfigure(2, weight = 1)
        canvas_lbl = tk.Label(entry_frame, image=canvas)
        canvas_lbl.image = canvas
        canvas_lbl.grid(column=0, row=0)
        stroke_lbl = tk.Label(entry_frame, image = stroke)
        stroke_lbl.image = stroke
        stroke_lbl.grid(column=1, row=0)
        subframe = tk.Frame(entry_frame)
        size_lbl = tk.Label(subframe, text=f"Size: {size}")
        size_lbl.pack()
        ratio_lbl = tk.Label(subframe, text=f"Ratio: {ratio}")
        ratio_lbl.pack()
        subframe.grid(column=2, row = 0)
        entry_frame.pack() 
    


