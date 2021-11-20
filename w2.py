# -*- coding: utf-8 -*-
"""W2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ntvpkWQ-oEbGJmcuTCmFcCeP0dz5zf7M
"""

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers.core import Dense,Activation,Flatten
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.preprocessing import image

#load data
(train_x, train_y), (test_x,test_y)= mnist.load_data()

#split the data
num_train = 2000
train_x = train_x[:num_train]
train_y = train_y[:num_train]

num_test = 2000
test_x = test_x[:num_test]
test_y = test_y[:num_test]

#convert input to one hot
np.set_printoptions(linewidth=200)
#print(np.array(train_x[0]))
x = np.array([[[1 if dd>0 else 0 for dd in m] for m in x] for x in train_x])
x_test = np.array([[[1 if dd>0 else 0 for dd in m] for m in x] for x in test_x])
#print(np.array(x[0]))

#convert target to one hot
#print(train_y[0])
y = tf.keras.utils.to_categorical(train_y)
y_test =  tf.keras.utils.to_categorical(train_y) 
#print(y[0])

num_uotput = y.shape[1]

 #model
 model = Sequential()

 model.add(Flatten(input_shape=(28,28)))
 model.add(Dense(512, activation='relu'))
 model.add(Dense(256, activation='relu'))
 model.add(Dense(128, activation='relu'))
 model.add(Dense(64, activation='relu'))
 
 model.add(Dense(num_uotput))
 model.add(Activation('sigmoid'))

 model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 history = model.fit(x,y, validation_data=(x_test,y_test), batch_size=1, epochs=10)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['loss'], label = 'loss')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

