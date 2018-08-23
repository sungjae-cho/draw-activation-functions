import numpy as np

def linear(x):
	y = np.copy(x)
	return y

def binary_threshold(x):
	y = np.copy(x)
	y[y > 0] = 1
	y[y <= 0] = 0
	return y

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def tanh(x):
	return np.tanh(x)

def relu(x):
	y = np.copy(x)
	y[y <= 0] = 0
	return y 	
