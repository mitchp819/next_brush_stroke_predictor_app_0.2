import numpy as np
import os
from PIL import Image
import pickle
from dataset import Dataset

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