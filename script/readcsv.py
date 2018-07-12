import csv
import numpy as np

def readCSV(name):
	x = open(name)
	csv_x = csv.reader(x)

	lx=[]

	for row in csv_x:
		lx.append(list(map(float, row)))

	return lx
