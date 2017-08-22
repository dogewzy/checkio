def checkio(data):

	def get_chunk(result):
		length_result = [len(_) for _ in result]
		record = []
		length = 0
		point = 0
		while point != len(length_result):
			chunk_len = length_result[point]
			for i in range(len(length_result)):
				if length_result[point] == chunk_len:
					length += 1
					point += 1
					if point == len(length_result):
						record.append((length, chunk_len))
						break
				else:
					record.append((length, chunk_len))
					length = 0
					break
		return record

	def determine_same_letter(need_process):
		exist = []
		for _ in need_process:
			if _[0] in exist:
				index_repeat = (exist.index(_[0]), len(exist), len(exist) - exist.index(_[0]))
				return True, index_repeat
			exist.append(_[0])
		return False

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

	def get_count(item, d):
		count = 0
		for each_letter in item:
			for _ in d:
				if each_letter in _:
					count += 1
		count -= len(item)
		return count

	def get_proper_order(data):
		p = [(get_count(i, data), i) for i in data]
		p.sort(key=lambda x: x[0], reverse=True)
		result = [x[1] for x in p]
		return result

	# remove the duplicate item
	data = get_proper_order(remove_duplicate_item(data))
	process_data = [list(i) for i in data]
	for each_data in process_data:
		if len(set(each_data)) != len(each_data):
			for _ in each_data:
				while each_data.count(_) > 1:
					each_data.remove(_)


	data = process_data
	print(data)
	result = list(data[0])
	mark = 0
	for each_data in data[1:]:
		flag = True
		for i in each_data:
			# if has same letter,joint them
			if i in result or i in [_[0] for _ in result]:
				i_index_in_eachdata = each_data.index(i)
				i_index_in_result = result.index(i) if i in result else [_[0] for _ in result].index(i)
				for k in each_data[:i_index_in_eachdata]:
					result.insert(i_index_in_result, k + str(mark))
					i_index_in_result += 1
				for k in each_data[i_index_in_eachdata + 1:]:
					result.insert(i_index_in_result + 1, k + str(mark))
					i_index_in_result += 1
				flag = False
				break
		# if have no same item,connect them
		if flag:
			if result[0] > each_data[0]:
				result = list(each_data) + result
			else:
				result += list(each_data)
		mark += 1
		# print(result, 'after a joint')

	# extract the item with 2-length that need be processed,for example, if c0 c1 both appear,we have to
	# handle the letter between them,there may be more than one need_process
	divide_chunk = get_chunk(result)
	ret = []
	point = 0
	for each_chunk in divide_chunk:
		if each_chunk[1] == 1:
			to_be_extend = [_ for _ in result[point:point+each_chunk[0]] if _ not in ret]
			ret.extend(to_be_extend)
			point += each_chunk[0]
		if each_chunk[1] == 2:
			need_process = result[point:point+each_chunk[0]]

			point += each_chunk[0]
			while type(determine_same_letter(need_process)) is tuple:
				print(need_process, 'np')
				index_repeat = determine_same_letter(need_process)[1]
				print(index_repeat,'oooooo')
				if index_repeat[2] == 1:
					need_process.pop(index_repeat[0])
				else:
					temp = need_process[index_repeat[0]:index_repeat[1] + 1]
					insert_index = 0
					pre_mark = temp[0][1]
					after_mark = temp[-1][1]
					# get the proper mark
					if index_repeat[0] > 0:
						if need_process[index_repeat[0] - 1][1] == need_process[index_repeat[0]][1]:
							mark = need_process[index_repeat[0] - 1][1]
					elif index_repeat[1] < len(need_process) - 1:
						if need_process[index_repeat[1] + 1][1] == need_process[index_repeat[1]][1]:
							mark = need_process[index_repeat[1] + 1][1]
					else:
						mark = need_process[index_repeat[0]][1]
					slice_frag = [temp[0][0] + mark]
					# change the mark for next process(maybe)
					for _ in temp[1:-1]:
						if _[1] == pre_mark:
							slice_frag.insert(insert_index + 1, _[0] + mark)
							insert_index += 1
						if _[1] == after_mark:
							slice_frag.insert(insert_index, _[0] + mark)
							insert_index += 1
					need_process = need_process[:index_repeat[0]] + slice_frag + need_process[index_repeat[1] + 1:]

			process_result = [_[0] for _ in need_process]
			print(ret, process_result,111111)
			ret.extend(process_result)
		# print(ret)

	return ''.join(ret)


print(checkio(["hello", "low", "lino", "itttnosw"]))
# print(checkio(["h","l","o"]))
# print(checkio(["acb","bd","zwa"]))
# print(checkio(["yagz","qwerty","asdfg","zxcvb"]))
# print(checkio(["is","not","abc","nots","iabcn"]))