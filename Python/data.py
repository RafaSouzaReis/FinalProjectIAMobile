from typing import List

class Data:
    def __init__(self, columns : List[float], classification : str):
        self.__columns__ = columns
        self.__classification__ = classification
        self.__distance__ : float = -1

    def get_columns(self):
        return self.__columns__

    def set_classifcation(self, classification : str):
        self.__classification__ = classification

    def get_classification(self):
        return self.__classification__

    def set_distance(self, new_distance : float):
        self.__distance__ = new_distance

    def get_distance(self):
        return self.__distance__
    
    
    
