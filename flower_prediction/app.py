import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    print(query_df)
    prediction = model.predict(query_df)
    return jsonify({"Prediction": list(prediction)})


if __name__ == '__main__':
    app.run(debug=True)
