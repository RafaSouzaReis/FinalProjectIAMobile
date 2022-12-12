from typing import List
from IA.data import Data
from IA.distance_generator import DistanceGenerator

class KNN:
    def __init__(self, k : int):
        self.__k__ = k
        self.__distance_generator__ = DistanceGenerator()

    def execute(self, newData : Data, data_collection : List[Data]):
        self.__distance_generator__.euclidean_distance(newData, data_collection)
        ordered_collection : List[Data] = sorted(data_collection, key = Data.get_distance)
        nearest_neighbors : List[Data] = ordered_collection[:self.__k__]
        classification_dict = dict()
        for neighbor in nearest_neighbors:
            if neighbor.get_classification() in classification_dict:
                classification_dict[neighbor.get_classification()] += 1
            else:
                classification_dict[neighbor.get_classification()] = 1
        newData.set_classifcation(max(classification_dict, key=classification_dict.get))

    
