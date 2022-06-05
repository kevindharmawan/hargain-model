import os

import numpy as np
import tensorflow as tf

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.before_first_request
def load_model():
    global model

    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, 'model/model.h5')

    model = tf.keras.models.load_model(path)
    print("Model loaded!")

@app.route('/predict', methods=['POST'])
def predict():
    required = ['cost', 'start_price', 'end_price', 'increment']
    data = request.get_json(force=True)

    for key in required:
        if key not in data:
            return jsonify({'error': 'Missing parameter: {}'.format(key)}), 400

    cost = data['cost']
    start_price = data['start_price']
    end_price = data['end_price']
    increment = data['increment']

    x = []

    while start_price < end_price:
        x.append([start_price, cost])
        start_price += increment

    predictions = model.predict([np.array(x)])

    result = []

    max_profit = 0
    optimal_price = 0

    for i in range(len(predictions)):
        price = float(x[i][0])
        sales = float(predictions[i][0])
        profit = float((price - cost) * sales)

        if profit > max_profit:
            max_profit = profit
            optimal_price = price

        result.append((price, sales, profit))

    return jsonify({
        "predictions": result,
        "optimal_price": optimal_price,
    })

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Harga.in Machine Learning API'

if __name__ == '__main__':
    app.run(debug=True)