import tkinter as tk
from PIL import Image, ImageTk

from data import DatasetValidation as dv, DataTransformation as dt

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data import Dataset


class EntryView:
    
    def __init__(self,container: tk, dataset:'Dataset'):
        main_frame = tk.Frame(container, bg = '#A822B2')
        self.create_entrys(main_frame, dataset)
        main_frame.pack(fill="x", padx=5, pady=5)

    def create_entrys(self, container:tk, cs_dataset:'Dataset'):
        #Does this need to be faster? 
        ds = cs_dataset.dataset
        row_count = cs_dataset.entry_count
        canvas_entrys = ds["canvas"]
        stroke_entrys = ds["stroke"]
        for row in range(0,row_count):
            holder_frame = tk.Frame(container)
            holder_frame.pack()
            lbl = tk.Label(holder_frame, text=f"Holder Frame {row}")
            lbl.pack()
            canvas = dt.np_image_to_tk(canvas_entrys[row])
            stroke = dt.np_image_to_tk(stroke_entrys[row])
            self.entry_row(holder_frame, canvas, stroke, "(100x100)", "1:1")

    
    def entry_row(self, container:tk.Widget, canvas:tk.PhotoImage, stroke:tk.PhotoImage, size:str =None, ratio:str = None):
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
        entry_frame.pack() 



        