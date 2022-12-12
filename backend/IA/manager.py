import csv
import random
from IA.data import Data
from IA.data_collection import DataCollection
from IA.distance_generator import DistanceGenerator
from IA.k_nearest_neighbor import KNN
from typing import List
from sklearn import metrics
import matplotlib.pyplot as plt  

class Manager:
    def __init__(self):
        self.__inner_headers__ : List[str] = list()
        self.__inner_data__ = DataCollection()
        self.__knn__ = KNN(3)
    
    def load_csv(self, file : str):
        data_set = csv.reader(open(file))
        self.__inner_headers__ = next(data_set)
        for line in data_set:
            self.__inner_data__.append_data(Data(line[:-1], line[-1]))

    def show_csv(self):
        print(self.__inner_headers__)
        self.__inner_data__.show_collection()

    def train_knn(self):
        originalDataCollection = self.__inner_data__.get_collection()
        random.shuffle(originalDataCollection)
        division = int(round(len(originalDataCollection)*0.25,0))
        dataTrain = originalDataCollection[division:]
        dataTest = originalDataCollection[:division]
        for data in dataTest:
            self.__knn__.execute(data, dataTrain)
        self.generate_confusion_matrix(dataTest, originalDataCollection[:division])


    def execute_knn(self, newDataFile):
        newRawData = csv.reader(newDataFile)
        newData : Data
        for line in newRawData:
            newData = Data(line[:], '?')
        self.__knn__.execute(newData, self.__inner_data__.get_collection())
        self.__inner_data__.append_data(newData)

    def generate_confusion_matrix(self, predicted : List[Data], actual : List[Data]):
        true_values : List[str] = list()
        predicted_values : List[str] = list()

        print("PREDICTED")
        for data_test in predicted:
            predicted_values.append(data_test.get_classification())
            print(data_test.get_classification())

        print("ACTUAL")
        for data_og in actual:
            true_values.append(data_og.get_classification())
            print(data_og.get_classification())

        confusion_matrix = metrics.confusion_matrix(true_values, predicted_values)

        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)

        cm_display.plot()

        plt.show()






