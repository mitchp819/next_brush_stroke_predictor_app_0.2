import numpy as np
import os
from PIL import Image, ImageTk
import pickle

WHITE_VALUE = 255
STROKE_DEFAULT_VALUE = -1


class DataTransformation:
    @staticmethod
    def np_image_to_png(image: np.ndarray, path: str):
        pil_image = Image.fromarray(image)
        pil_image.save(path)
        
    @staticmethod
    def scale_np_image(image: np.ndarray, scale: float) -> np.ndarray:
        new_height = int(image.shape[0] * scale)
        new_width = int(image.shape[1] *scale)
        resized_np = DataTransformation.transform_np_image(image, new_width, new_height)
        return resized_np
    
    @staticmethod
    def transform_np_image(image: np.ndarray, new_width: int, new_height: int) -> np.ndarray:
        """
        Transforms a np.array image to a new width and height
        """
        pil_image = Image.fromarray(image)
        resized_image = DataTransformation.transform_pil_image(pil_image, new_width, new_height)
        resized_np = np.array(resized_image)
        return resized_np

    @staticmethod
    def transform_pil_image(pil_image: Image, new_width:int=None, new_height:int=None,):
        img_width, img_height = pil_image.size
        if new_width != None and new_height == None:
            scale:float = new_width / img_width
            new_height = int(img_height * scale)
        elif new_width == None and new_height != None:
            scale:float = new_height / img_height
            new_width = int(img_width * scale)
        elif new_width == None and new_height == None:
            new_width = img_width
            new_height = img_height

        resized_image = pil_image.resize(
            (new_width, new_height),
            resample = Image.NEAREST) 
        return resized_image

    @staticmethod
    def set_pixel_color(image: np.ndarray, x:int, y:int, color:int):
        image[x,y] = color
    
    @staticmethod
    def np_image_to_tk(image:np.ndarray, new_width: int = None, new_height = None):
        pil_image = Image.fromarray(image, mode= "L")
        tk_image = ImageTk.PhotoImage(pil_image)
        return tk_image


