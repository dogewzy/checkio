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
		l = length - 1
		while sorted_list[j] >= sorted_list[l]:
			l -= 1
		sorted_list[j], sorted_list[l] = sorted_list[l], sorted_list[j]
		part1 = sorted_list[:j + 1]
		part2 = [i for i in reversed(sorted_list[j + 1:])]
		sorted_list = part1 + part2
		result.append(''.join(sorted_list))


def possible_situation(marbles: str, step: int):
	last_line = dict()
	length = len(marbles)
	for w_num in range(length + 1):
		key = 'w' * w_num + 'b' * (length - w_num)
		diff = marbles.count('w') - w_num
		no_diff = (step - 1 - abs(diff))
		if no_diff % 2 != 0 or step - 1 - abs(diff) < 0:
			continue
		else:
			cycle = int(no_diff / 2)
			change = []
			[change.append('w') for _ in range(diff)] if diff > 0 else [change.append('b') for _ in range(-diff)]
			[change.extend(['w', 'b']) for _ in range(cycle)]
			last_line[key] = algorithm_L(sorted(change))
	return last_line


def checkio(marbles: str, step: int):
	last_line = possible_situation(marbles, step)
	result = 0
	for k, v in last_line.items():
		p1 = k.count('w') / len(k)
		p2 = 0
		for each_permutation in v:
			temp = 1
			w_count = marbles.count('w')
			b_count = marbles.count('b')
			for each_change in each_permutation:
				if each_change == 'w':
					temp *= w_count / len(k)
					w_count -= 1
					b_count += 1
				elif each_change == 'b':
					temp *= b_count / len(k)
					b_count -= 1
					w_count += 1
			p2 += temp
		result += p1 * p2
	return round(result, 2)


# other's fucking solution in recursion way
# my only advantage is that my solution is not recursion
# but his is more clear
def checkio2(marbles, step):
	def getProb(white, total, step):
		P = (1.0 * white / total if white > 0 else 0) if white < total else 1
		return (
			P * getProb(white - 1, total, step - 1) + (1.0 - P) * getProb(white + 1, total, step - 1)) if step > 0 else P
	return round(getProb(marbles.count('w'), len(marbles), step - 1), 2)


def checkio3(marbles, step):
	mlist_in = [(marbles, 1)]
	for i in range(step):
		mlist_out = []
		if i != step - 1:
			for s in mlist_in:
				wn = s[0].count("w")
				if wn == len(s[0]):
					mlist_out.append(("w" * (wn - 1) + "b", s[1]))
				elif wn == 0:
					mlist_out.append(("w" + "b" * (len(s[0]) - 1), s[1]))
				else:
					mlist_out.append(("w" * (wn - 1) + "b" * (len(s[0]) - wn + 1), s[1] * float(wn) / len(s[0])))
					mlist_out.append(("w" * (wn + 1) + "b" * (len(s[0]) - wn - 1), s[1] * (1 - float(wn) / len(s[0]))))
			mlist_in = mlist_out[:]
		else:
			result = 0
			for s in mlist_in:
				wn = s[0].count("w")
				result += float(wn) / len(s[0]) * s[1]

	return result

t = [checkio,checkio2,checkio3]
for i in t:
	a = time.time()
	i("bbbwwbbbww", 20)
	print(time.time() - a)

