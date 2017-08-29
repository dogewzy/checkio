def checkio(matrix):
	result = True
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i == j:
				result = result and matrix[i][j] == 0
			else:
				result = result and matrix[i][j] == -matrix[j][i]
	return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-2, -1, 0]]) == True, "1st example"
	assert checkio([
		[0, 1, 2],
		[-1, 1, 1],
		[-2, -1, 0]]) == False, "2nd example"
	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-3, -1, 0]]) == False, "3rd example"
