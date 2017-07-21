
def checkio(data):
	result = 0

	def real_cal(data,result):
		if data:
			result += data.pop()
			result = real_cal(data,result)
		return result

	return real_cal(data,result)


print(checkio([1, 2, 3, 4]))
