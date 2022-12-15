import pandas as pd
import random
from IA.data import Data
from IA.data_collection import DataCollection
from IA.distance_generator import DistanceGenerator
from IA.k_nearest_neighbor import KNN
from typing import List
from sklearn import metrics
import matplotlib.pyplot as plt
import io
import base64

class Manager:
    def __init__(self):
        self.__inner_headers__ : List[str] = list()
        self.__inner_data__ = DataCollection()
        self.__knn__ = KNN()
    
    def load_csv(self, file : str):
        dataframe = pd.read_csv(file)
        if len(dataframe.columns) == 1:
            dataframe = pd.read_csv(file, sep=";")
        self.update_data_collection(dataframe)
        self.update_k()
        self.__inner_headers__ = dataframe.columns

    def update_data_collection(self, df):
        columns = df.columns
        for index in df.index:
            new_data : List[str] = list()
            for column in columns:
                new_data.append(df[column][index])
            self.__inner_data__.append_data(Data(new_data[:-1],new_data[-1]))

    def update_k(self):
        self.__knn__.set_k(round(len(self.__inner_data__.get_collection())*0.15))

    def shuffle_collection(self):
        random.shuffle(self.__inner_data__.get_collection())

    def train_knn(self):
        copyDataCollection : List[Data] = list()
        self.shuffle_collection()

        for item in self.__inner_data__.get_collection():
            copyDataCollection.append(Data(item.get_columns(), item.get_classification()))

        division = int(round(len(copyDataCollection)*0.7,0))
        dataTest = copyDataCollection[division:]

        for data in dataTest:
            self.__knn__.execute(data, copyDataCollection[:division])

        return self.generate_confusion_matrix(dataTest, self.__inner_data__.get_collection()[division:])

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
        list_labels : List[str] = list()

        for data_test, data_og in zip(predicted, actual):
            predicted_values.append(data_test.get_classification())
            if not data_test.get_classification() in list_labels:
                list_labels.append(data_test.get_classification())
            true_values.append(data_og.get_classification())
            if not data_og.get_classification() in list_labels:
                list_labels.append(data_og.get_classification())

        confusion_matrix = metrics.confusion_matrix(true_values, predicted_values)

        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels=list_labels)

        cm_display.plot()

        plt.savefig('./IA/Result/foo.png', bbox_inches='tight')

        image = None
        with io.BytesIO() as buffer:
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image = base64.b64encode(buffer.getvalue()).decode()
        return image