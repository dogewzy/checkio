VOWELS = "aeiouy"


def translate(phrase: str):
	split_word = phrase.split(' ')
	result = ''
	for idx, every_word in enumerate(split_word):
		for vowel in VOWELS:
			if vowel * 3 in every_word:
				every_word = every_word.replace(vowel * 3, vowel)
		every_word = list(every_word)
		del_record = []
		for index, letter in enumerate(every_word):
			if letter not in VOWELS:
				del_record.append(index + 1)
		[every_word.pop(_) for _ in sorted(del_record, reverse=True)]
		if idx != 0:
			result += (' '+''.join(every_word))
		else:
			result += ''.join(every_word)
	return result


print(translate("hoooowe yyyooouuu duoooiiine"))
