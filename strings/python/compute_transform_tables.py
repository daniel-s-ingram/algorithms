#!/usr/bin/env python
def compute_transform_tables(X, Y, cC, cR, cD, cI):
	X = list(X)
	Y = list(Y)
	m = len(X)
	n = len(Y)

	costs = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
	ops = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

	for i in xrange(1, m+1):
		costs[i][0] = i*cD
		ops[i][0] = 'D%c' % X[i-1]

	for i in xrange(1, n+1):
		costs[0][i] = i*cI
		ops[0][i] = 'I%c' % Y[i-1]

	for i in xrange(1, m+1):
		for j in xrange(1, n+1):
			if X[i-1] == Y[j-1]:
				costs[i][j] = costs[i-1][j-1] + cC
				ops[i][j] = 'C%c' % X[i-1]
			else:
				costs[i][j] = costs[i-1][j-1] + cR
				ops[i][j] = 'R%c' % X[i-1] + str(Y[j-1])

			if costs[i-1][j] + cD < costs[i][j]:
				costs[i][j] = costs[i-1][j] + cD
				ops[i][j] = 'D%c' % X[i-1]

			if costs[i][j-1] + cI < costs[i][j]:
				costs[i][j] = costs[i][j-1] + cI
				ops[i][j] = 'I%c' % Y[j-1]

	return costs, ops

if __name__ == '__main__':
	costs, ops = compute_transform_tables('Mason Lee Slate', 'What a hoodangable nightmare', -1, 1, 2, 2)

	print 'Costs'
	for row in costs:
		print row

	print 'Operations'
	for row in ops:
		print row

