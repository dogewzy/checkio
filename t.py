global_mark = 0


def find_duplicate(result, data=None):
	"""
	return whether marked letter in data appear in result
	:param result: master list
	:param data: the data need to be combine,if None,do result self check
	:return: (boolean, mark)mark is a tuple that the pending letter carry with,if mark is empty and
	boolean is True,means the same letter in result has no mark
	"""
	pass


def result_merge(result, data, mark):
	"""
	merge the data to result.
	find the chunk with "mark of result" in result!!
	condition 1:mark of result is None, just insert
	condition 2:not None, call mask_merge(chunk, data)
	:param mark: tuple (mark of result, mark of data),the value return from find_duplicate()
	:return: result
	"""
	pass


def result_self_clean(result):
	"""
	result may have same letter(with or without mark) after be merged with data.
	remove the duplicate letter .
	condition 1:(with mark1, with mark2)  adjust the letters order between them,if there are more than 2 marks
	between them,move the mark3,mark4... out of the clean place first. eg: [a0b0 c1 d2 f3 k4a4],
	first adjust to [a0b0 k4a4 c1d2f3],then call mark_merge() to get the result [k5a5b5 c1 d2 f3]
	condition 2:(with, without) remove the letter without mark,think about it for a minute
	than check the result again
	:param result:
	:return: cleaned result
	"""


def mark_merge(data1, data2):
	"""
	merge two lists which have same letter
	:param data1: list1 with mark1
	:param data2: list2 with mark2
	:return: merge list with new mark3
	"""


def clean_input(data):
	"""
	remove duplicate letter,sort in the order of information amount
	"""
	data = get_proper_order(remove_duplicate_item(data))
	return data


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