def checkio(data):
	from collections import namedtuple
	point = namedtuple('point', ('x', 'y'))
	points = [point(_[0], _[1]) for _ in data]
	point1 = points[0]
	total_area = 0.0
	for point2, point3 in zip(points[1:], points[2:]+[point1]):
		total_area += ((point2.x - point1.x) * (point3.y - point1.y) - (point2.y - point1.y) * (point3.x - point1.x)) / 2
	return abs(total_area)


# print(checkio([[1, 2], [3, 8], [9, 8]]))  # 18
# print(checkio([[1, 2], [3, 8], [7, 1]]))  # 22
print(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]))
# if __name__ == '__main__':
# 	#This part is using only for self-checking and not necessary for auto-testing
# 	def almost_equal(checked, correct, significant_digits=1):
# 		precision = 0.1 ** significant_digits
# 		return correct - precision < checked < correct + precision
#
# 	assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
# 	assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
# 	assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
# 	assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
# 	assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
# 	assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
