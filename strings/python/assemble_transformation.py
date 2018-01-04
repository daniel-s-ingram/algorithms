from compute_transform_tables import compute_transform_tables

def assemble_transformation(ops, i, j):
	if i == 0 and j == 0:
		seq = []
		return seq
	else:
		if ops[i][j][0] == 'C' or ops[i][j][0] == 'R':
			seq = assemble_transformation(ops, i-1, j-1)
			seq.append(ops[i][j])
			return seq
		elif ops[i][j][0] == 'D':
			seq = assemble_transformation(ops, i-1, j)
			seq.append(ops[i][j])
			return seq
		else:
			seq = assemble_transformation(ops, i, j-1)
			seq.append(ops[i][j])
			return seq

if __name__ == '__main__':
	_, operations = compute_transform_tables('Mason Lee Slate', 'What a hoodangable nightmare', -1, 1, 2, 2)

	m = len(operations)
	n = len(operations[0])
	sequence = assemble_transformation(operations, m-1, n-1)
	
	file = open('min_cost.txt', 'w')

	string = list('Mason Lee Slate')
	i = 0
	cost = 0
	for op in sequence:
		if op[0] == 'C':
			file.write('%-16s' % 'Copy %c' % op[1])
			file.write('\t\t\t' + ''.join(string))
			file.write('\r\n')
			
			i += 1
			cost -= 1
		elif op[0] == 'R':
			string[i] = op[2]

			file.write('%-16s' % ('Replace %c' % op[1] + ' with ' + str(op[2])))
			file.write('\t\t' + ''.join(string))
			file.write('\r\n')
			
			i += 1
			cost += 1
		elif op[0] == 'D':
			string.pop(i)

			file.write('%-16s' % 'Delete %c' % op[1])
			file.write('\t\t\t' + ''.join(string))
			file.write('\r\n')
			
			i += 1
			cost += 2
		else:
			string.insert(i, op[1])

			file.write('%-16s' % 'Insert %c' % op[1])
			file.write('\t\t\t' + ''.join(string))
			file.write('\r\n')
			
			i += 1
			cost += 2

	file.write('\r\nMinimum cost: ' + str(cost))
	file.close()