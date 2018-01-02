#!/usr/bin/env python
from swap import swap

def insertion_sort(array):
	n = len(array)

	for i in xrange(1, n):
		j = i
		while array[j] < array[j-1] and j > 0:
			swap(array, j, j-1)
			j = j-1

	return array

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	sorted_array = insertion_sort(array.copy())
	print 'Original:', array
	print 'Sorted:', sorted_array