#!/usr/bin/env python
from swap import swap

def insertion_sort(array, n):
	for i in xrange(1, n):
		j = i
		while array[j] < array[j-1] and j > 0:
			swap(array, j, j-1)
			j = j-1

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	print 'Original:', array
	insertion_sort(array, n)
	print 'Sorted:', array