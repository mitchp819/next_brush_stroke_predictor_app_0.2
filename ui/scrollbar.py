import tkinter as tk
from tkinter import ttk


class ScrollContainer:
    @staticmethod
    def create_scrollbar(container, width, height) -> ttk.Frame:
        scroll_canvas = tk.Canvas(container, width=width, height=height)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command = scroll_canvas.yview)
        scrollbar.pack(side='right', fill='y')
        scroll_canvas.pack(side = 'left', fill='both', expand=True)
        scroll_canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_frame = ttk.Frame(scroll_canvas)
        scroll_canvas.create_window((0,0), window= scrollable_frame, anchor='nw')
        scrollable_frame.bind(
            "<Configure>", lambda event: ScrollContainer.on_configure(event, scroll_canvas))
        scroll_canvas.bind_all(
            "<MouseWheel>", lambda event: ScrollContainer.on_mouse_wheel(event, scroll_canvas))
        return scrollable_frame

    @staticmethod
    def on_configure(event, scroll_canvas:tk.Canvas):
        scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all'))
        scroll_canvas.itemconfigure("window", width = event.width)
        pass

    @staticmethod
    def on_mouse_wheel(event, scroll_canvas: tk.Canvas):
        scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")