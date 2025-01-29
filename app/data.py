import tkinter as tk
import numpy as np
import pandas as pd
import time

WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DrawingData:
    def __init__(self):
        self.data = {
            "canvas":       [],
            "stroke":       []
        }
        self.dataframe = pd.DataFrame(self.data)
    

class CanvasData:
    def __init__(self, width: int, height: int):
        self.data = np.ones((width, height), dtype= np.uint8) * WHITE_VALUE
    
    def update(self, x, y, value):
        self.data[x, y] = value

class StrokeData:
    def __init__(self, width: int, height: int):
        self.data = np.full((width, height), fill_value= STROKE_DEFAULT_VALUE, dtype=np.uint8)
    
    def update(self, x, y, value):
        self.data[x, y] = value
