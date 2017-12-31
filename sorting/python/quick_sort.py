#!/usr/bin/env python
from swap import swap

def partition(array, l, r):
	p = array[r]
	j = l-1

	for i in xrange(l, r):
		if array[i] < p:
			j = j+1
			swap(array, i, j)

	if array[r] < array[j+1]:
		swap(array, j+1, r)

	return j+1

def quick_sort(array, l, r):
	if l < r:
		p = partition(array, l, r)

		quick_sort(array, l, p-1)
		quick_sort(array, p+1, r)

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	print 'Original:', array
	quick_sort(array, 0, n-1)
	print 'Sorted:', array