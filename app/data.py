import tkinter as tk
import numpy as np
import pandas as pd
import time
from PIL import Image, ImageTk, ImageGrab

WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DataTransformation:
    @staticmethod
    def scale_np_image(image: np, scale):
        pass
    
    @staticmethod
    def transform_np_image(image: np, new_width: int, new_height: int) -> np:
        """
        Transforms a np.array image to a new width and height
        """
        pil_image = Image.fromarray(image)
        resized_image = pil_image.resize(
            (new_width, new_height),
            resample = Image.NEAREST)
        resized_np = np.array(resized_image)
        return resized_np

class Dataset:
    def __init__(self, *fields):
        self.fields = fields
        self.entry_count = 0
        self.dataset = {}
        for arg in fields :
            self.dataset[arg] = []
        pass

    def __str__(self):
        return f'{self.dataset}\nEntry Count: {self.entry_count}\nFields: {self.fields}'
    
    def insert(self, entry):
        if isinstance(entry, tuple):
            self.insert_tuple(entry)
            return
        if isinstance(entry, dict):
            self.insert_dict(entry)
            return
        raise ValueError("Entry must be type tuple or dict")
    
    def insert_tuple(self, entry: tuple):
        if len(self.fields) != len(entry):
            raise ValueError(f"Entry length != number of fields \nEntry: {entry}")
        for key, value in zip(self.dataset.keys(), entry):
            self.dataset[key].append(value)
        self.entry_count += 1
        pass

    def insert_dict(self, entry: dict):
        pass

class CanvasDataController:
    def __init__(self):
        dataset = Dataset("canvas", "stroke")
        dataset.insert((11,12))
        dataset.insert((21,22))
        print(dataset)
        pass


if __name__ == "__main__":
    CanvasDataController()
    pass