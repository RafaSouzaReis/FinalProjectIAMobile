import pandas as pd
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
        dataframe = pd.read_csv(file, sep=";")
        columns = dataframe.columns
        for index in dataframe.index:
            new_data : List[str] = list()
            for column in columns:
                new_data.append(dataframe[column][index])
            self.__inner_data__.append_data(Data(new_data[:-1],new_data[-1]))

    def train_knn(self):
        copyDataCollection : List[Data] = list()

        for item in self.__inner_data__.get_collection():
            copyDataCollection.append(Data(item.get_columns(), item.get_classification()))

        division = int(round(len(copyDataCollection)*0.7,0))
        dataTrain = copyDataCollection[:division]
        dataTest = copyDataCollection[division:]

        for data in dataTest:
            self.__knn__.execute(data, dataTrain)

        self.generate_confusion_matrix(dataTest, self.__inner_data__.get_collection()[division:])


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

        for data_test in predicted:
            predicted_values.append(data_test.get_classification())

        for data_og in actual:
            true_values.append(data_og.get_classification())

        confusion_matrix = metrics.confusion_matrix(true_values, predicted_values)

        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)

        cm_display.plot()

        plt.savefig('./IA/Result/foo.png', bbox_inches='tight')





