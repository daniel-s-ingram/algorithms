#!/usr/bin/env python
from swap import swap

def selection_sort(array, n):
	for i in xrange(n):
		for j in xrange(i, n):
			if array[j] < array[i]:
				swap(array, i, j)

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	print 'Original:', array
	selection_sort(array, n)
	print 'Sorted:', array