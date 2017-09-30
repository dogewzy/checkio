def get_can_cap(caped_index, has_cap, num, matrix):
	result = set()
	for idx in range(num):
		if matrix[caped_index][idx] == 1:
			if idx not in has_cap:
				result.add(idx)
	return result


def capture(matrix):
	num = len(matrix)
	has_cap = {0}
	wait = {}
	time = 0
	while len(has_cap) != num:
		for i in has_cap:
			for _ in get_can_cap(i, has_cap, num, matrix):
				if _ not in wait:
					wait[_] = matrix[_][_]
		time += 1
		del_dick = []
		for k in wait:
			wait[k] -= 1
			if wait[k] == 0:
				del_dick.append(k)
				has_cap.add(k)
		[wait.pop(k) for k in del_dick]
	return time

print(capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]))