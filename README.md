**Model  Tutorial**

Save Tensorflow model as `model.h5` in `model/` folder

Run program using flask `python -m flask run`

Run program from file `py app.py` or `python app.py` or `python3 app.py`

**API Documentation**

Price Prediction

URL : `/predict`
Method : `POST`
Input: cost, start_price, end_price, increment, category
Output: prediction, optimal_price

API Testing

URL : `/`
Method : `GET`
Output: "Welcome to Harga.in Machine Learning API"
