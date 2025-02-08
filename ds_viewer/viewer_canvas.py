from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data import Dataset

class ViewerInterface:
    def __init__(self, dataset:Dataset):
        pass