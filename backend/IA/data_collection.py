from typing import List
from IA.data import Data


class DataCollection:
    def __init__(self):
        self.__collection__ : List[Data] = list()

    def append_data(self, entry : Data):
        self.__collection__.append(entry)

    def show_collection(self):
        for entry in self.__collection__:
            print(entry.get_columns(), "Distance: ", entry.get_distance(), " Class:  ", entry.get_classification() )
            
    def get_data(self, index : int):
        return self.__collection__[index]

    def get_collection(self):
        return self.__collection__
