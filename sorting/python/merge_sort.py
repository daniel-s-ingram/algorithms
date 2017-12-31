#!/usr/bin/env python

def merge(array, l, m, r):
	#Determine the length of the left and right subarrays
	l_n = m-l+1
	r_n = r-m

	#Create the left and right subarrays
	L = [0]*l_n
	R = [0]*r_n

	#Fill the left and right subarrays with the appropriate values from the original array
	i = j = 0
	while i < l_n or j < r_n:
		if i < l_n:
			L[i] = array[l+i]
			i = i+1
		
		if j < r_n:
			R[j] = array[m+j+1]
			j = j+1

	#Increment through the left and right subarrays, each of which has already been sorted by previous recursive calls, and merge them
	#into a single sorted subarray within the original array; k is the location of the merged element in the original array
	i = j = 0
	k = l
	while i < l_n and j < r_n:
		if L[i] > R[j]:
			array[k] = R[j]
			j = j + 1
		else:
			array[k] = L[i]
			i = i + 1
		
		k = k + 1

	#Grab any remaining elements in the left OR right subarrays (these elements were greater than any of the elements in the other subarray)
	while i < l_n:
		array[k] = L[i]
		i = i + 1
		k = k + 1

	while j < r_n:
		array[k] = R[j]
		j = j + 1
		k = k + 1

def merge_sort(array, l, r):
	#As long as the array has more than one element, divide it in two and recursively call merge_sort and then merge
	if l < r:
		m = (l+r)/2
		
		merge_sort(array, l, m)
		merge_sort(array, m+1, r)

		merge(array, l, m, r)

if __name__ == '__main__':
	import numpy as np
	
	n = 100
	array = np.random.randint(100, size=n)
	
	print 'Original:', array
	merge_sort(array, 0, n-1)
	print 'Sorted:', array