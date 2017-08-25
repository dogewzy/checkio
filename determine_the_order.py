def pop_last(order_set: set, total_letter: set, order: list):
	letter_at_front = [_[0] for _ in order_set]
	end_letters = total_letter.difference(letter_at_front)
	[total_letter.remove(i) for i in end_letters]

	def change(_):
		if _[1] in end_letters:
			return '#' + _[0]
		else:
			return _

	new_order_set = set([change(_) for _ in order_set])
	order = (sorted(list(end_letters))) + order
	return new_order_set, total_letter, order


def divide_data(data):
	association_item = set()
	for item in data:
		for another_item in data:
			if not set(item).isdisjoint(set(another_item)) and item != another_item:
				association_item.update({item, another_item})
	isolation_item = set(data).difference(association_item)
	return association_item, isolation_item


def process_isolate_part(isolate_part: set):
	result = []
	while isolate_part:
		# print(isolate_part)
		pop_item = min(isolate_part)
		isolate_part.remove(pop_item)
		if len(pop_item) > 1:
			isolate_part.add(pop_item[1:])
		result.append(pop_item[0])
	return result


def process_associate_part(associate_part: set):
	order = []
	total_letter = set()
	[total_letter.update(set(x)) for x in associate_part]
	total_length = len(total_letter)
	order_set = set()
	for each_data in associate_part:
		[order_set.add(a + b) for a, b in zip(each_data[:-1], each_data[1:])]
	while len(order) != total_length:
		order_set, total_letter, order = pop_last(order_set, total_letter, order)
	return ''.join(order)


def checkio(data):
	"""
	first we have to devide the data into two parts,the part we use the order in str and another part that
	use the order in latin alphabetical order.
	for the associate part.eg 'abg','dgo',we extract the pattern[ab,bg,dg,go],always can find a letter only appears in
	the behalf part of pattern,than the insert into the tail of result
	"""
	from collections import OrderedDict
	data = [''.join(OrderedDict.fromkeys(_)) for _ in data]
	associate_part, isolate_part = divide_data(data)
	order = process_associate_part(associate_part)
	if order:
		isolate_part.add(order)
	result = process_isolate_part(isolate_part)
	return result