from operator import mul


def checkio(number):
	little = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	result = []
	while number != 1:
		for i in little:
			if i == 1:
				return 0
			if number % i == 0:
				little = little[little.index(i):]
				result.append(i)
				number = number / i
				break

	sorted(result)
	digit = [10 ** i for i in range(len(result))]
	io = sum(map(mul, result, digit))

	return io


print(checkio(19))
