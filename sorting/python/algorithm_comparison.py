#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort

n_powers = 4
n_elements = [0]*n_powers
for i in xrange(n_powers):
	n_elements[i] = 10**(i+1)

selection_times = [0]*n_powers
insertion_times = [0]*n_powers
merge_times = [0]*n_powers
quick_times = [0]*n_powers
counting_times = [0]*n_powers

file = open('README.md', 'w')
file.write('n\t\t\t\t\t')
for i in xrange(n_powers):
	if i is not n_powers-1:
		file.write("%-10d" % n_elements[i] +'\t\t\t')
	else:
		file.write("%-10d" % n_elements[i] +'\r\n\n')

array = [0, 0, 0, 0]
for i in xrange(n_powers):
	array[i] = np.random.randint(100, size=n_elements[i])

file.write('Selection sort\t\t')
for i in xrange(n_powers):
	selection_time = timeit(stmt='selection_sort(array[i].copy())', setup="from __main__ import array, selection_sort, i", number=1)
	selection_times[i] = selection_time

	file.write("%0.2e" % selection_time)
	
	if i is not n_powers-1:
		file.write(' s\t\t\t')
	else:
		file.write(' s\r\n')

file.write('Insertion sort\t\t')
for i in xrange(n_powers):
	insertion_time = timeit(stmt='insertion_sort(array[i].copy())', setup="from __main__ import array, insertion_sort, i", number=1)
	insertion_times[i] = insertion_time
	
	file.write("%0.2e" % insertion_time)
	
	if i is not n_powers-1:
		file.write(' s\t\t\t')
	else:
		file.write(' s\r\n')

file.write('Merge sort\t\t\t')
for i in xrange(n_powers):
	merge_time = timeit(stmt='merge_sort(array[i].copy(), 0, n_elements[i]-1)', setup="from __main__ import array, merge_sort, i, n_elements", number=1)
	merge_times[i] = merge_time

	file.write("%0.2e" % merge_time)
		
	if i is not n_powers-1:
		file.write(' s\t\t\t')
	else:
		file.write(' s\r\n')

file.write('Quick sort\t\t\t')
for i in xrange(n_powers):
	quick_time = timeit(stmt='quick_sort(array[i].copy(), 0, n_elements[i]-1)', setup="from __main__ import array, quick_sort, i, n_elements", number=1)
	quick_times[i] = quick_time

	file.write("%0.2e" % quick_time)
	
	if i is not n_powers-1:
		file.write(' s\t\t\t')
	else:
		file.write(' s\r\n')

file.write('Counting sort\t\t')
for i in xrange(n_powers):
	counting_time = timeit(stmt='counting_sort(array[i].copy())', setup="from __main__ import array, counting_sort, i", number=1)
	counting_times[i] = counting_time

	file.write("%0.2e" % counting_time)
	
	if i is not n_powers-1:
		file.write(' s\t\t\t')
	else:
		file.write(' s\r\n')

file.close()

x = np.log10(n_elements)
plt.plot(x, selection_times)
plt.plot(x, insertion_times)
plt.plot(x, merge_times)
plt.plot(x, quick_times)
plt.plot(x, counting_times)

plt.show()