from flask import Flask
from IA.manager import Manager

app = Flask(__name__)

@app.route('/')
def start():
    #application = Manager()
    #application.load_csv('./IA/lol.txt')
    #application.train_knn()
    print('oie')

if __name__ == '__main__':
    app.run()