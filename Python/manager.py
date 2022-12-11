import csv
import random
from data import Data
from data_collection import DataCollection
from distance_generator import DistanceGenerator
from k_nearest_neighbor import KNN
from typing import List
from sklearn import metrics
import matplotlib.pyplot as plt  

class Manager:
    def __init__(self):
        self.__inner_headers__ : List[str] = list()
        self.__inner_data__ = DataCollection()
        self.__knn__ = KNN(3)
    
    def load_csv(self):
        data_set = csv.reader(open('lol.txt'))
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
        for newData in dataTest:
            self.__knn__.execute(newData, dataTrain)
        self.generate_confusion_matrix(dataTest, division)
        self.show_csv()


    def execute_knn(self, newDataFile):
        newRawData = csv.reader(newDataFile)
        newData : Data
        for line in newRawData:
            newData = Data(line[:], '?')
        self.__knn__.execute(newData, self.__inner_data__.get_collection())
        self.__inner_data__.append_data(newData)

    def generate_confusion_matrix(self, tested : List[Data], division : int):
        true_values : List[str] = list()
        predicted_values : List[str] = list()
        for data_og in (self.__inner_data__.get_collection())[:division]:
            true_values.append(data_og.get_classification())
            print(data_og.get_classification())

        for data_test in tested:
            predicted_values.append(data_test.get_classification())
            print(data_test.get_classification())

        confusion_matrix = metrics.confusion_matrix(true_values, predicted_values)

        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

        cm_display.plot()

        plt.show()






