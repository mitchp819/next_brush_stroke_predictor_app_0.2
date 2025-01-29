import tkinter as tk
from tkinter import ttk
from typing import Literal
import numpy as np
import pandas as pd
from PIL import Image
import os
import re

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
    print("Error: windll not imported. Text may be blurred")
    pass

from app import (  ImageProcessor, BrushTool, AppConsole, greyscale_value_to_hex, shape_img,
                  get_a_DATABASE, get_LOADED_DB, get_last_file_by_id, 
                  canvas_np_img_to_png, UI_COLOR, ASSETS_DIR, DATA_DIR, 
                  SIMILAR_IMAGES_DIR
)

class DrawingData():
    MAX_MARK_HISTORY = 10
    STROKE_DEAFULT_VALUE = -1
    WHITE_VALUE = 255
    def __init__(self, image_width: int = 128, image_height: int = 128):
        """
        Holds the canvas data.
        Args:
            image_width: int        width of the image
            image_height: int       height of the image
        """
        self.image_width = image_width
        self.image_height = image_height
        self.data = {
            "canvas":       [],
            "stroke":       [],
            "line_type":    [],
            "speed":        [],
            "ratio":        [],
            "color_type":   [],
        }
        self.dataframe = pd.DataFrame(self.data)
        self.canvas_data = self.white_canvas()
        self.last_save_canvas_data = self.white_canvas()
        self.stroke_data = self.blank_stroke()
        self.prev_stroke_data = []
        pass

    def white_canvas(self):
        return np.ones((self.image_width, self.image_height), dtype= np.uint8) * self.WHITE_VALUE
   
    def blank_stroke(self):
        return np.full((self.image_width, self.image_height), fill_value= self.STROKE_DEAFULT_VALUE, dtype=np.uint8)

    def create_mark(self, x1: int, y1: int, x2: int, y2: int, brush_color: str):
        """
        Adds mark data to canvas_data and stroke_data.

        Args:
            x1: int             left bound
            y1: int             top bound
            x2: int             right bound
            y2: int             bottom bound
            brush_color: str    color of mark
        """
        if len(self.prev_stroke_data) > self.MAX_MARK_HISTORY:
            self.prev_stroke_data.pop()
        self.prev_stroke_data.append(self.stroke_data.copy())

        for x in range(x1, x2):
            for y in range(y1, y2):
                if (x < self.image_width and x >= 0 and y < self.image_height and y >= 0):
                    self.canvas_data[y, x] = brush_color
                    self.stroke_data[y, x] = brush_color 
        
        pass

    def save_stroke_to_dataset(self):
        """
        Saves (canvas, stroke, attributes 1, ..., attribute n) data to dataset.
        """


        pass

class DrawingCanvas(ttk.Frame):
    def __init__(self, container: ttk.Frame, frame_scalor: int = 6, image_width: int = 128, image_height: int = 128):
        """
        Holds the drawing canvas.

        Args:
            container: ttk.Frame    parent frame
            frame_scalor: int       scales the frame size
            image_width: int        width of the image
            image_height: int       height of the image
        """
        super().__init__(container)
        self.container = container
        self.frame_scalor = frame_scalor
        self.image_width = image_width
        self.image_height = image_height
        self.frame_width = self.image_width * self.frame_scalor
        self.frame_height = self.image_height * self.frame_scalor
        self.brush_tool = None
        self.data_gather_tool = None
        self.app_console = None
        self.gen_tool = None
        self.info_pane = None
        
        main_frame = tk.Frame(self,border=3, relief='raised', bg=UI_COLOR)
        main_frame.pack()
        
        self.canvas = tk.Canvas(main_frame, 
                                width=self.frame_width, 
                                height=self.frame_height, 
                                bg='white',
                                border=2,
                                relief='groove'
                                )
        self.canvas.pack(pady=10,padx=10)
        self.pack(side=tk.LEFT, expand= True)

        self.drawing_data = DrawingData(image_width=self.image_width, image_height=self.image_height)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.create_mark)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_released)
        pass
    
    def set_brush_tool(self, brush_tool: BrushTool):
        self.brush_tool = brush_tool
    def set_data_gather_tool(self, data_gather_tool):
        self.data_gather_tool = data_gather_tool
    def set_app_console(self, app_console):
        self.app_console = app_console
    def set_gen_tool(self, gen_tool):
        self.gen_tool = gen_tool
    def set_info_pane(self, info_pane):
        self.info_pane = info_pane

    def on_mouse_down(self, event):
        """
        Records the initial mouse click position.
        """
        pass

    def on_mouse_released(self, event):
        if self.data_gather_tool.get_data_gather_mode() == 'auto':
            self.save_stroke_to_dataset()   
        pass

