def checkio(a, b, c):
	import math
	largest = max(a, b, c)
	if largest >= a + b + c - largest:
		return [0, 0, 0]
	cos1 = (a * a + b * b - c * c) / (2.0 * a * b)
	cos2 = (a * a + c * c - b * b) / (2.0 * a * c)
	cos3 = (b * b + c * c - a * a) / (2.0 * b * c)

	return sorted(round(math.degrees(math.acos(cos))) for cos in [cos1, cos2, cos3])


print(checkio(3, 4, 5))
