import os 
import pickle

class PickleIO:
    @staticmethod
    def load(path: str):
        path = os.path.abspath(path)
        with open(path, 'rb') as f:
            return pickle.load(f)
    
    @staticmethod
    def save(data, path: str):
        if not path.endswith((".pkl",)):
            os.path.join(path, ".pkl")
        with open(path, 'wb') as f:
            pickle.dump(data, f)


class DatasetValidation:
    @staticmethod
    def entry_matches_fields(entry: tuple, fields: tuple):
        if len(fields) != len(entry):
            raise ValueError(f"Entry length != number of fields \nEntry: {entry}")
    
    @staticmethod
    def col_len_match(current_length, prev_lenght):
        try:
            if prev_lenght != None and current_length != prev_lenght:
                raise ValueError("Column lengths do not match")
        except ValueError as e:
                print(f"Error: {e}")
    
    @staticmethod
    def validate_dataset(dataset: dict):
        field_list = []
        prev_col_len: int = None
        for key, value in dataset.items():
            field_list.append(key)
            current_col_len = len(value)
            DatasetValidation.col_len_match(current_col_len , prev_col_len)
            prev_col_len = current_col_len 
        return prev_col_len
    

class DatasetTransformation:
    @staticmethod
    def cat_datasets():
        pass

class Dataset:
    """
    Stores data in a Dictionary.
    Args
        *fields: Define column headers
    """
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
        DatasetValidation.entry_matches_fields(entry, self.fields)
        for key, value in zip(self.dataset.keys(), entry):
            self.dataset[key].append(value)
        self.entry_count += 1


    def insert_dict(self, entry: dict):
        raise ValueError("Dictionaries not configured")

    def save(self,  location: str = None, name:str = None):
        path = os.path.join(location, name)
        PickleIO.save(self.dataset, path)

    def load(self, path: str):
        ds = PickleIO.load(path)
        entry_count = DatasetValidation.validate_dataset(ds)
        self.dataset = ds
        self.entry_count = entry_count
        self.fields = tuple(ds.keys())

