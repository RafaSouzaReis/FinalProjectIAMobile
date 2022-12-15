from flask import Flask, request, jsonify
import json
from IA.manager import Manager
from io import StringIO
import matplotlib

app = Flask(__name__)
matplotlib.use('agg')


@app.route('/', methods=['POST'])
def start():
    if not request.data:
        return jsonify({"erro": "Corpo vazio"}), 400

    try:
        json_data = request.get_json()
    except json.JSONDecodeError:
        return jsonify({"erro": "Json invalido"}), 400

    try:
        csv = json_data['csv']
    except KeyError:
        return jsonify({"erro": "Csv nao encontrado"}), 400

    KNN = Manager()
    KNN.load_csv(StringIO(csv))
    imagem = KNN.train_knn()

    return jsonify({"sucesso": True, "imagem": imagem})


if __name__ == '__main__':
    app.run()