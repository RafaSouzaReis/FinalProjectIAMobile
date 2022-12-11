from data import Data
from manager import Manager

if __name__ == '__main__':
    application = Manager()
    application.load_csv()
    application.train_knn()