from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Activation, LSTM
from keras.layers import SimpleRNN
from keras.datasets import imdb
from window_stride import readData_concat
import random
import csv
import numpy as np

stride = 1
window = 1
(x_all, y_all) = readData_concat(['01.csv', '02.csv', '03.csv', '04.csv', '05.csv', '06.csv', '07.csv', '08.csv'], stride, window)

lx_len = len(x_all)
ly_len = len(y_all)
print(lx_len)
tempzip = []
for i in range(lx_len):
	tempzip.append((x_all[i], y_all[i]))
random.shuffle(tempzip)
lxx=[]
lyy=[]
for i in range(lx_len):
	(ta, tb) = tempzip[i]
	lxx.append(np.array(ta))
	lyy.append(np.array(tb))
lx_train = lxx[0 : int(lx_len * 4 / 5)]
ly_train = lyy[0 : int(ly_len * 4 / 5)]
lx_test = lxx[int(lx_len * 4 / 5):]
ly_test = lyy[int(ly_len * 4 / 5):]

model = Sequential()
model.add(Dense(64, input_dim = window * 62))
model.add(Activation("relu"))
model.add(Dense(32))
model.add(Activation("relu"))
model.add(Dense(len(y_all[0])))
model.add(Activation("softmax"))
model.compile(loss = "mean_squared_error", optimizer = "rmsprop", metrics = ["accuracy"])
model.fit(np.array(lx_train), np.array(ly_train), batch_size = 50, nb_epoch = 10)
loss_a = model.evaluate(np.array(lx_test), np.array(ly_test), batch_size = 128)
print(loss_a)
