
from flask import Flask, Response, jsonify
from flask_restplus import Api, Resource, fields, reqparse
from flask_cors import CORS, cross_origin
import os
from keras import Sequential
from keras.layers import LSTM, Dense
from keras import metrics

app = Flask(__name__)

port = int(os.getenv('PORT', 8080))

@app.route('/', methods=['POST'])
def index():   #Needs to be a list of last 50 pollution observations

    pollutionData = app.request.args['sensorData']
    model = Sequential()
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam', metrics=[metrics.mae, metrics.categorical_accuracy])

    model.load_weights("model.h5", by_name=True)

    predictedAQI = model.predict(pollutionData)
    return jsonify({'result': predictedAQI[0]})  # Returning most recent prediction

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port, debug=False) # deploy with debug=False
    app.run(debug=True, use_reloader=True)
