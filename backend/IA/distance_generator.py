from IA.data import Data
from IA.data_collection import DataCollection
import math

class DistanceGenerator:

    def euclidean_distance(self, newData : Data, data_collection : DataCollection):
        sum : float
        for oldData in data_collection:
            sum = 0
            for oldDataColumn, newDataColumn in zip(oldData.get_columns(), newData.get_columns()):
                sum += math.pow(float(oldDataColumn) - float(newDataColumn), 2)
            oldData.set_distance(math.sqrt(sum))
        
    

