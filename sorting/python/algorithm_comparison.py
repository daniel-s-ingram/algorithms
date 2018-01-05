#!/usr/bin/env python
# -*- coding: latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort

#Converts to a more readable scientific notation with formatting for .md superscript
def readable_sn(sn):
	sn = '%e' % sn
	base, exponent = sn.split('e')
	return (base + '×10<sup>%s</sup>' % exponent)

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
file.write('|n|')
for i in xrange(n_powers):
	if i is not n_powers-1:
		file.write(str(n_elements[i]) +'|')

file.write('\r\n\n')

file.write('|---:|')
for _ in xrange(n_powers):
	file.write(':---:|')
file.write('\r\n')

array = [0, 0, 0, 0]
for i in xrange(n_powers):
	array[i] = np.random.randint(100, size=n_elements[i])

file.write('|**Selection sort**|')
for i in xrange(n_powers):
	selection_time = timeit(stmt='selection_sort(array[i].copy())', setup="from __main__ import array, selection_sort, i", number=1)
	selection_times[i] = selection_time

	file.write(readable_sn(selection_time) + ' s|')
file.write('\r\n')

file.write('|**Insertion sort**|')
for i in xrange(n_powers):
	insertion_time = timeit(stmt='insertion_sort(array[i].copy())', setup="from __main__ import array, insertion_sort, i", number=1)
	insertion_times[i] = insertion_time
	
	file.write(readable_sn(insertion_time) + ' s|')
file.write('\r\n')

file.write('|**Merge sort**|')
for i in xrange(n_powers):
	merge_time = timeit(stmt='merge_sort(array[i].copy(), 0, n_elements[i]-1)', setup="from __main__ import array, merge_sort, i, n_elements", number=1)
	merge_times[i] = merge_time

	file.write(readable_sn(merge_time) + ' s|')
file.write('\r\n')

file.write('|**Quick sort**|')
for i in xrange(n_powers):
	quick_time = timeit(stmt='quick_sort(array[i].copy(), 0, n_elements[i]-1)', setup="from __main__ import array, quick_sort, i, n_elements", number=1)
	quick_times[i] = quick_time

	file.write(readable_sn(quick_time) + ' s|')
file.write('\r\n')

file.write('|**Counting sort**|')
for i in xrange(n_powers):
	counting_time = timeit(stmt='counting_sort(array[i].copy())', setup="from __main__ import array, counting_sort, i", number=1)
	counting_times[i] = counting_time

	file.write(readable_sn(counting_time) + ' s|')
file.write('\r\n')

file.close()

#Needs scale adjustment - maybe separate graphs for different orders of time complexity
#x = np.log10(n_elements)
#plt.plot(x, selection_times)
#plt.plot(x, insertion_times)
#plt.plot(x, merge_times)
#plt.plot(x, quick_times)
#plt.plot(x, counting_times)

#plt.show()