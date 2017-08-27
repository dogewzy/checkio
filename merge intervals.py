def merge_intervals(intervals: list):
	"""
		Merge overlapped intervals.
	"""
	result = []
	while len(intervals) > 1:
		first, second = intervals[0], intervals[1]
		key_num = first[1]
		if key_num < second[0] - 1:
			result.append(first)
			intervals = intervals[1:]
		if second[0]-1 <= key_num < second[1]:
			intervals = intervals[2:]
			intervals.insert(0, (first[0], second[1]))
		if key_num >= second[1]:
			intervals.remove(second)
	result.extend(intervals)
	return result
print(merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]))