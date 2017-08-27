def get_longest_chunk_length(can_use: list):
	length = 0
	temp_length = 0
	for _ in range(len(can_use)):
		if can_use[_] == 1:
			temp_length += 1
			if _ == len(can_use) - 1:
				length = max(length, temp_length)
		if can_use[_] == 0:
			length = max(length, temp_length)
			temp_length = 0
	return length


def largest_histogram(histogram: list):
	result = 0
	can_use = [0 for _ in histogram]
	height_sort = sorted(set(histogram), reverse=True)
	for height in height_sort:
		for _ in [i for i, _ in enumerate(histogram) if _ == height]:
			can_use[_] = 1
		length = get_longest_chunk_length(can_use)
		result = max(result, height * length)
	return result


if __name__ == "__main__":
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert largest_histogram([5]) == 5, "one is always the biggest"
	assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
	assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
	assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
	assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
	print("Done! Go check it!")
