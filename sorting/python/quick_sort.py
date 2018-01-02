#!/usr/bin/env python
from swap import swap

def partition(array, l, r):
	if l <= r:
		p = array[r]
		j = l

		for i in xrange(l, r):
			if array[i] < p:
				swap(array, i, j)
				j = j+1

		swap(array, j, r)
		return j

def quick_sort(array, l, r):
	if l < r:
		p = partition(array, l, r)

		array = quick_sort(array, l, p-1)
		array = quick_sort(array, p+1, r)

	return array

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	sorted_array = quick_sort(array.copy(), 0, n-1)
	print 'Original:', array
	print 'Sorted:', sorted_array