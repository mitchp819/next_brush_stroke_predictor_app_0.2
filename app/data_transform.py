import numpy as np
import os
from PIL import Image
import pickle
from dataset import Dataset

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
        resized_image = pil_image.resize(
            (new_width, new_height),
            resample = Image.NEAREST)
        resized_np = np.array(resized_image)
        return resized_np
    
    



class TestDataset:
    def __init__(self):
        dataset = Dataset("canvas", "stroke")
        #dataset.insert((11,12))
        #dataset.insert((21,22))
        #dataset.save("data", "test")
        dataset.load("data\\test.pkl")
        print(dataset)

        pass


if __name__ == "__main__":
    TestDataset()
    pass