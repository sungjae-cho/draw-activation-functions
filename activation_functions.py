import numpy as np

def linear(x):
	return x

def binary_threshhold(x):
	if x > 0:
		return 1
	else:
		return 0

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def tanh(x):
	return np.tanh(x)

def relu(x):
	if x > 0:
		return x
	else:
		return 0	
