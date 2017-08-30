import time

def algorithm_L(sorted_list: list):
	result = [''.join(sorted_list)]
	length = len(sorted_list)
	if length in {0, 1}:
		return result
	j = length - 2
	while j != -1:
		j = length - 2
		while sorted_list[j] >= sorted_list[j + 1]:
			j -= 1
			if j == -1:
				return result
		l = length-1
		while sorted_list[j] >= sorted_list[l]:
			l -= 1
		sorted_list[j], sorted_list[l] = sorted_list[l], sorted_list[j]
		part1 = sorted_list[:j+1]
		part2 = [i for i in reversed(sorted_list[j+1:])]
		sorted_list = part1 + part2
		result.append(''.join(sorted_list))


def possible_situation(marbles: str, step: int):
	last_line = dict()
	length = len(marbles)
	for w_num in range(length+1):
		key = 'w' * w_num + 'b' * (length - w_num)
		diff = marbles.count('w') - w_num
		no_diff = (step - 1 - abs(diff))
		if no_diff % 2 != 0 or step - 1 - abs(diff) < 0:
			continue
		else:
			cycle = int(no_diff/2)
			change = []
			[change.append('w') for _ in range(diff)] if diff > 0 else [change.append('b') for _ in range(-diff)]
			[change.extend(['w', 'b']) for _ in range(cycle)]
			print(change,'change')
			last_line[key] = algorithm_L(sorted(change))
	return last_line


def checkio(marbles: str, step: int):
	last_line = possible_situation(marbles, step)
	print(last_line)
	result = 0
	for k, v in last_line.items():
		p1 = k.count('w')/len(k)
		p2 = 0
		for each_permutation in v:
			temp = 1
			w_count = marbles.count('w')
			b_count = marbles.count('b')
			for each_change in each_permutation:
				if each_change == 'w':
					temp *= w_count/len(k)
					w_count -= 1
					b_count += 1
				elif each_change == 'b':
					temp *= b_count / len(k)
					b_count -= 1
					w_count += 1
			p2 += temp
		result += p1 * p2
	return round(result, 2)


print(checkio("wwwwwwwwwwwwwwwwwwww",20))
#
#
#
# if __name__ == '__main__':
# 	assert checkio('bbw', 3) == 0.48, "1st example"
# 	assert checkio('wwb', 3) == 0.52, "2nd example"
# 	assert checkio('www', 3) == 0.56, "3rd example"
# 	assert checkio('bbbb', 1) == 0, "4th example"
# 	assert checkio('wwbb', 4) == 0.5, "5th example"
# 	assert checkio('bwbwbwb', 5) == 0.48, "6th example"
