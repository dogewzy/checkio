from itertools import count

mark = count(0, 1)


def get_proper_order(data):
	p = [(get_count(i, data), i) for i in data]
	p.sort(key=lambda x: x[0], reverse=True)
	result = [x[1] for x in p]
	return result


def get_count(item, d):
	count = 0
	for each_letter in item:
		for _ in d:
			if each_letter in _:
				count += 1
	count -= len(item)
	return count


def remove_duplicate_item(data):
	from copy import deepcopy
	kk = deepcopy(data)
	for i in range(len(kk)):
		for each_data in kk:
			if kk[i] in each_data and kk.index(each_data) != i:
				print(each_data, i)
				data.remove(kk[i])
				break
	return data


def clean_input(data):
	"""
	remove duplicate letter,sort in the order of information amount
	"""
	data = get_proper_order(remove_duplicate_item(data))
	return data


def find_duplicate(result, data=None):
	"""
	return whether marked letter in data appear in result
	:param result: master list
	:param data: the data need to be combine,if None,do result self check
	:return: (boolean, mark)mark is a tuple that the pending letter carry with,if mark is empty and
	boolean is True,means the same letter in result has no mark
	"""
	is_duplicate = False
	strip_mark_result = [_[0] for _ in result]
	if not data:
		if len(result) == len(set(strip_mark_result)):
			return [is_duplicate, 0, 0]
		else:
			for letter in strip_mark_result:
				if strip_mark_result.count(result) == 2:
					is_duplicate = True
					first_index = strip_mark_result.index(letter)
					second_index = strip_mark_result[first_index:].index(letter) + first_index
					return [is_duplicate, first_index, second_index]
	else:
		for letter in data:
			if letter in strip_mark_result:
				is_duplicate = True
				result_mark = result[strip_mark_result.index(letter)][1]
				data_mark = next(mark)
				return [is_duplicate, result_mark, str(data_mark)]
		data_mark = next(mark)
		return [is_duplicate, None, str(data_mark)]


def result_self_clean(result, index1, index2):
	"""
	result may have same letter after be merged with data.
	remove the duplicate letter .
	:param result:
	:return: cleaned result
	"""
	_mark_1 = result[index1][1:]
	_mark_2 = result[index2][1:]
	chunk1 = [_ for _ in result if _[1:] == _mark_1]
	chunk2 = [_ for _ in result if _[1:] == _mark_2]
	print(chunk1, chunk2, 'chunk')
	new = mark_merge(chunk1, chunk2)
	print(new)
	print(result[:index1], new, result[index1+len(chunk1)+1:index2], result[index2+len(chunk2):])
	return list(result[:index1]) + new + list(result[index1+len(chunk1)+1:index2]) + list(result[index2+len(chunk2):])


def origin_taste(result):
	"""
	get origin order'abcdefg...' to the result chunk can't merge
	"""
	index_record = [0]
	mark_record = [result[0][1]]
	new = []
	for letter in result:
		if letter[1:] not in mark_record:
			mark_record.append(letter[1:])
			index_record.append(result.index(letter))
	strip_result = [_[0] for _ in result]
	chunks = [strip_result[start:end] for start, end in zip(index_record, index_record[1:]+[len(result)])]
	while chunks:
		little = min([_[0] for _ in chunks])
		for chunk in chunks:
			if little == chunk[0]:
				new.append(little)
				chunk.pop(0)
				if not chunk:
					chunks.remove([])
	return ''.join(new)


def mark_merge(data1, data2):
	"""
	merge two lists which have same letter
	:param data1: list1 with mark1
	:param data2: list2 with mark2
	:return: merge list with new mark(may be lots of marks)
	"""
	strip_data1, strip_data2 = [_[0] for _ in data1], [_[0] for _ in data2]
	for data_index, letter in enumerate(strip_data2):
		if letter in strip_data1:
			insert_index = strip_data1.index(letter)
			_mark = str(next(mark))
			chunk_data1_left = [_+_mark for _ in strip_data1[:insert_index]]
			_mark = str(next(mark))
			chunk_data1_right = [_+_mark for _ in strip_data1[insert_index+1:]]
			_mark = str(next(mark))
			chunk_data2_left = [_+_mark for _ in strip_data2[:data_index]]
			_mark = str(next(mark))
			chunk_data2_right = [_+_mark for _ in strip_data2[data_index+1:]]
			print(chunk_data1_left,chunk_data2_left,chunk_data1_right,chunk_data2_right,99999999)
			chunks = [*sorted([chunk_data1_left, chunk_data2_left]), [letter+str(next(mark))], *sorted([chunk_data1_right, chunk_data2_right])]
			from itertools import chain
			ret = []
			[ret.extend(_) for _ in chain(chunks)]
			return ret


def checkio(inpt):
	inpt = clean_input(inpt)
	_mark = next(mark)
	result = [_+str(_mark) for _ in inpt[0]]
	for each_data in inpt[1:]:
		is_duplicate, result_mark, data_mark = find_duplicate(result, each_data)
		if not is_duplicate:
			[result.append(i+data_mark) for i in each_data]
		else:
			result_chunk = [letter for letter in result if letter.endwith(result_mark)]
			to_be_merge_chunk = [letter+data_mark for letter in each_data]
			start, end = result.index(result_mark[0]), result.index(result_mark[-1])
			new_chunk = mark_merge(result_chunk, to_be_merge_chunk)
			result = result[:start] + new_chunk + result[end:]
			duplicate_flag = True
			while duplicate_flag:
				duplicate_flag, index1, index2 = find_duplicate(result)
				if not duplicate_flag:
					break
				else:
					result = result_self_clean(result, index1, index2)
	return result


# a = origin_taste(['a0','c0','b11','d11','g3','k4','f4'])
# print(a)
# b = mark_merge(['a1','b1','t1'], ['i2','b2','c2','g2'])
# print(b)
c = result_self_clean(['ax','cx','ay','dy','gp','kq','fq'],0,2)
print(c)