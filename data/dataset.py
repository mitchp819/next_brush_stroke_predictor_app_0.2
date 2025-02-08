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
    def validate_dataset(dataset: dict, expected_fields:list = None):
        """
        Checks if all columns have the same number of rows 

        Returns number of rows 
        """
        field_list = []
        prev_col_len: int = None
        for key, value in dataset.items():
            field_list.append(key)
            current_col_len = len(value)
            DatasetValidation.col_len_match(current_col_len , prev_col_len)
            prev_col_len = current_col_len 
        if expected_fields != None:
            DatasetValidation.compare_fields(expected_fields, field_list)
        print(f"Dataset Valid. Fields: {str(field_list)}")
        return prev_col_len
    
    @staticmethod
    def compare_fields(expected_fields, real_fields):
        for expected_field in expected_fields:
            field_exists = False
            for real_field in real_fields:
                if expected_field == real_field:
                    field_exists = True
            try:
                if field_exists == False:
                    raise ValueError(f"Expected Field: {expected_field}, not found in dataset. Dataset Fields: {str(real_fields)}")
            except ValueError as e:
                print(f"Error: {e}")

class DatasetTransformation:
    @staticmethod
    def cat_datasets():
        pass

class Dataset:
    """
    Stores data in a Dictionary.
    Args
        *fields: Define column headers
    Functions
        append: add element to end of dataset (entry)
        save: save dataset to folder (location, name)
        load: load an existing pickeled dataset
        get_entry: returns entry at an (index)
        set_entry: Overwrites an entry at an (index)
        delete_entry: Deletes an entry at an (index)
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
    
    def append(self, entry):
        if isinstance(entry, tuple):
            self.append_tuple(entry)
            return
        if isinstance(entry, dict):
            self.append_dict(entry)
            return
        raise ValueError("Entry must be type tuple or dict")
    
    def append_tuple(self, entry: tuple):
        DatasetValidation.entry_matches_fields(entry, self.fields)
        for key, value in zip(self.dataset.keys(), entry):
            self.dataset[key].append(value)
        self.entry_count += 1

    def append_dict(self, entry: dict):
        #TODO hand inserting dictionarys (should handle dicts with multiple entrys?)
        raise ValueError("Dictionaries not configured")

    def save(self,  location: str = None, name:str = None):
        path = os.path.join(location, name)
        PickleIO.save(self.dataset, path)

    def load(self, path: str, expected_fields: list = None):
        ds: dict = PickleIO.load(path)
        entry_count = DatasetValidation.validate_dataset(ds, expected_fields)
        self.dataset = ds
        self.entry_count = entry_count
        self.fields = tuple(ds.keys())

    def get_entry(self, index:int) -> tuple:
        entry = []
        for value in self.dataset.values():
            entry.append(value[index])
        return tuple(entry)
    
    def set_entry(self, index:int, new_entry:tuple):
        """
        WARNING function overwrites data at the index
        """
        DatasetValidation.entry_matches_fields(new_entry, self.fields)
        for ds_value, entry_value in zip(self.dataset.values(), new_entry):
            ds_value[index] = entry_value
    
    def delete_entry(self, index: int):
        for value in self.dataset.values():
            del value[index]
