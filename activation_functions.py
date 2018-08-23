import numpy as np

def linear(x):
	return x

def binary_threshold(x):
	x[x > 0] = 1
	x[x <= 0] = 0
	return x

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def tanh(x):
	return np.tanh(x)

def relu(x):
	x[x <= 0] = 0
	return x 	
