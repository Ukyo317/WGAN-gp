import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import collections
import time
import pickle as pickle

_since_beginning = collections.defaultdict(lambda: {})
_since_last_flush = collections.defaultdict(lambda: {})

_iter = [0]
def tick():
	_iter[0] += 1

def plot(name, value):
	_since_last_flush[name][_iter[0]] = value

def flush():
	prints = []

	for name, vals in _since_last_flush.items():
		#prints.append("{}\t{}".format(name, np.mean(vals.values())))
		val = []
		for value_ in vals.values():
			val.append(value_)
		prints.append("{}\t{}".format(name, np.mean(val)))
		_since_beginning[name].update(vals)

		x_vals_key = []
		for k in _since_beginning[name].keys():
			x_vals_key.append(k)

		x_vals = np.sort(x_vals_key)
		y_vals = [_since_beginning[name][x] for x in x_vals]

		plt.clf()
		plt.plot(x_vals, y_vals)
		plt.xlabel('iteration')
		plt.ylabel(name)
		plt.savefig(name.replace(' ', '_')+'.jpg')

	print ("iter {}\t{}".format(_iter[0], "\t".join(prints)))
	_since_last_flush.clear()

	with open('log.pkl', 'wb') as f:
		pickle.dump(dict(_since_beginning), f, pickle.HIGHEST_PROTOCOL)