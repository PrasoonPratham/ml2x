import tensorflow as tf

train_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")

model.fit(train_data, test_data, epochs=500)
