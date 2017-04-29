from readcsv import readCSV
import random

def readData(names, stride, window):
	new_data_list_x = []
	new_data_list_y = []

	for i in range(len(names)):
		label = [0]*len(names)
		label[i] = 1

		lx = readCSV(names[i])
		
		x_new = []
		y_new = []

		i = 0
		while (i < len(lx) - window):
			x_new.append(lx[i : i + window])
			y_new.append(label)
			i = i + stride
		
		random.shuffle(x_new)
		x_new = x_new[0 : 400]
		y_new = y_new[0 : 400]
		new_data_list_x.append(x_new)
		new_data_list_y.append(y_new)


	x_all = new_data_list_x[0]
	y_all = new_data_list_y[0]
	for i in range(1, len(new_data_list_x)):
		x_all += new_data_list_x[i]
		y_all += new_data_list_y[i]

	return (x_all, y_all)


def readData_concat(names, stride, window):
	new_data_list_x = []
	new_data_list_y = []

	for i in range(len(names)):
		label = [0]*len(names)
		label[i] = 1

		lx = readCSV(names[i])
		random.shuffle(lx)
		lx = lx[0:4096]
		
		x_new = []
		y_new = []

		i = 0
		while (i < len(lx) - window):
			x_new_temp = []
			for k in range(i, i + window):
				x_new_temp += lx[k]
			x_new.append(x_new_temp)
			y_new.append(label)
			i = i + stride
		
		new_data_list_x.append(x_new)
		new_data_list_y.append(y_new)


	x_all = new_data_list_x[0]
	y_all = new_data_list_y[0]
	for i in range(1, len(new_data_list_x)):
		x_all += new_data_list_x[i]
		y_all += new_data_list_y[i]

	return (x_all, y_all)
