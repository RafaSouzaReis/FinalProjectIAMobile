from typing import List
from IA.data import Data
from IA.distance_generator import DistanceGenerator

class KNN:
    def __init__(self):
        self.__k__ = 1
        self.__distance_generator__ = DistanceGenerator()

    def execute(self, newData : Data, data_collection : List[Data]):
        self.__distance_generator__.euclidean_distance(newData, data_collection)
        ordered_collection : List[Data] = sorted(data_collection, key = Data.get_distance)
        nearest_neighbors : List[Data] = ordered_collection[:self.__k__]
        classification_dict = self.find_nearest_neighbors(nearest_neighbors)
        newData.set_classifcation(max(classification_dict, key=classification_dict.get))
        
    def find_nearest_neighbors(self, nearest_neighbors):
        classification_dict = dict()
        for neighbor in nearest_neighbors:
            if neighbor.get_classification() in classification_dict:
                classification_dict[neighbor.get_classification()] += 1
            else:
                classification_dict[neighbor.get_classification()] = 1
        return classification_dict
        
    def set_k(self, k : int):
        self.__k__ = k

    
