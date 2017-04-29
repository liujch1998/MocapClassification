from sklearn.cluster import KMeans
from readcsv import readCSV
import random
import numpy as np

dataset_names = ['01.csv', '02.csv', '03.csv', '04.csv', '05.csv', '06.csv', '07.csv', '08.csv']

X = []
y = []
counters = []
for i in range(len(dataset_names)):
	lx = readCSV(dataset_names[i])
	random.shuffle(lx)
	lx = lx[0:4000]
	X += lx
	y += [i] * len(lx)
	counters.append([0] * len(dataset_names))

print(len(X))

kmeans = KMeans(n_clusters = len(dataset_names), max_iter = 1000, n_init = 20, algorithm = "full").fit(np.array(X))

for i in range(0, len(kmeans.labels_)):
	counters[y[i]][kmeans.labels_[i]] = counters[y[i]][kmeans.labels_[i]] + 1

for i in range(0, len(counters)):
	print(counters[i])