import matplotlib.pyplot as plt
import numpy as np

fnn = np.array([
0.6023,
0.9336,
0.9592,
0.9707,
0.9741,
0.9823,
0.9866,
0.9895,
0.9923,
0.9929,
0.993,
0.9926,
0.9934,
0.9934,
0.9931,
0.9932,
0.9934,
0.9938,
0.9936,
0.9937])
rnn = np.array([
0.5981,
0.8626,
0.9147,
0.9339,
0.9599,
0.9744,
0.9829,
0.9893,
0.9893,
0.9927,
0.9902,
0.9932,
0.9949,
0.9936,
0.9945,
0.9953,
0.9962,
0.9966,
0.9979,
0.9983])
lstm = np.array([
0.6045,
0.8976,
0.9505,
0.9765,
0.9915,
0.9932,
0.9962,
0.9962,
0.9966,
0.9974,
0.9979,
0.9979,
0.9983,
0.9987,
0.9987,
0.9987,
0.9987,
0.9991,
0.9987,
0.9991])
#plt.plot(fnn)
#plt.plot(rnn)
#plt.plot(lstm)
plt.xticks(range(20))
plt.semilogy([1]-fnn)
plt.semilogy([1]-rnn)
plt.semilogy([1]-lstm)
plt.title('Neural Network Learning Curve')
plt.xlabel('epoch')
plt.ylabel('miss rate')
plt.legend(['Feed-forward NN','RNN','LSTM'])
plt.show()

