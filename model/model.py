
# Creating LSTM model for prediction

from keras import Sequential
from keras.layers import LSTM, Dense
from keras import metrics
from model.data_tranform import scaler, test_x, train_X, test_X, train_y, test_y
import matplotlib.pyplot as plt
from numpy import concatenate
from math import sqrt
from sklearn.metrics import mean_squared_error

model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam', metrics=[metrics.mae, metrics.categorical_accuracy])
history = model.fit(train_X, train_y, epochs=40, batch_size=52, validation_data=(test_X, test_y))

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

model.save("model.h5")

print("Model created and saved successfully.")
