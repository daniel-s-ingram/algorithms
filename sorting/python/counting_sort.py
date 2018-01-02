#!/usr/bin/env python

def counting_sort(array):
	n = len(array)
	k = max(array)+1

	count = [0]*k
	output = [0]*n

	for i in xrange(n):
		count[array[i]] = count[array[i]] + 1

	total = 0
	for j in xrange(k):
		less = count[j]
		count[j] = total
		total = total+less

	for i in xrange(n):
		output[count[array[i]]] = array[i]
		count[array[i]] = count[array[i]] + 1

	return output

if __name__ == '__main__':
	import numpy as np

	n = 100
	array = np.random.randint(100, size=n)

	print 'Original:', array
	sorted_array = counting_sort(array)
	print 'Sorted:', sorted_array