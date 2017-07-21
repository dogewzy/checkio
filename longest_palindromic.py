def longest_palindromic(text):
	from attrdict import AttrDict
	result = AttrDict(half_length=0, index=0)
	text = '#' + '#'.join(text) + '#'
	for index, _ in enumerate(text):
		half_length = 0
		for distance in range(1, min(index, len(text) - index) + 1):
			print(distance, index)
			if index + distance < len(text):
				# if not equal , quiet the foo loop
				if text[index + distance] == text[index - distance]:
					half_length += 1
					# print(half_length, index)
					if half_length > result.half_length:
						result.half_length, result.index = half_length, index
				else:
					break

	start = result.index - result.half_length
	end = result.index + result.half_length + 1
	print(result, start, end)
	return text[start:end].replace('#', '')


print(longest_palindromic("abc"))
