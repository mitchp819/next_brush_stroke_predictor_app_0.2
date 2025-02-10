import tkinter as tk

from data import DatasetValidation as dv, DataTransformation as dt

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data import Dataset


class EntryView:
    
    def __init__(self,container: tk, dataset:'Dataset'):
        main_frame = tk.Frame(container, bg = '#A822B2')
        lbl = tk.Label(main_frame, text="Entry View")
        lbl.pack(padx=3,pady=3)
        EntryView.create_entrys(main_frame, dataset)
        main_frame.pack(fill="x", padx=5, pady=5)
    
    @staticmethod 
    def create_entrys(container:tk.Widget, cs_dataset:'Dataset'):
        ds = cs_dataset.dataset
        row_count = cs_dataset.entry_count
        canvas_entrys = ds["canvas"]
        stroke_entrys = ds["stroke"]




    @staticmethod
    def create_entrys2(container:tk, cs_dataset:'Dataset'):
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
            #dt.np_image_to_png(canvas_entrys[row], f"canvas{row}r.png")
            canvas = dt.np_image_to_tk(canvas_entrys[row])
            stroke = dt.np_image_to_tk(stroke_entrys[row])
            #EntryRow(holder_frame, canvas, stroke, "(100x100)", "1:1")
            EntryView.entry_row(holder_frame, canvas, stroke, "(100x100)", "1:1")

    
    @staticmethod
    def entry_row(container:tk.Widget, canvas:tk.PhotoImage, stroke:tk.PhotoImage, row: int, size:str =None, ratio:str = None):
        entry_frame = tk.Frame(container)
        entry_frame.columnconfigure(0, weight = 3)
        entry_frame.columnconfigure(1, weight = 3)
        entry_frame.columnconfigure(2, weight = 1)
        canvas_lbl = tk.Label(entry_frame, image=canvas)
        canvas_lbl.grid(column=0, row=0)
        stroke_lbl = tk.Label(entry_frame, image = stroke)
        stroke_lbl.grid(column=1, row=0)
        sub_frame = tk.Frame(entry_frame)
        sub_frame.columnconfigure(0,weight=1)
        size_lbl = tk.Label(sub_frame, text = f"Size: {size}")
        size_lbl.grid(column = 0, row= 0)
        ratio_lbl = tk.Label(sub_frame, text=f"Ratio: {ratio}")
        ratio_lbl.grid(column=0, row=1)
        entry_frame.pack()

class EntryRow:
    def __init__(self, container:tk.Widget, canvas:tk.PhotoImage, stroke:tk.PhotoImage, size:str =None, ratio:str = None):
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
        
        sub_frame = tk.Frame(entry_frame)
        sub_frame.columnconfigure(0,weight=1)
        size_lbl = tk.Label(sub_frame, text = f"Size: {size}")
        size_lbl.grid(column = 0, row= 0)
        ratio_lbl = tk.Label(sub_frame, text=f"Ratio: {ratio}")
        ratio_lbl.grid(column=0, row=1)
        

        