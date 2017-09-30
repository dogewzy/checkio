def verify_anagrams(first_word, second_word):
	first_word = [word.upper() for word in first_word]
	second_word = [word.upper() for word in second_word]
	d1, d2 = {}, {}
	[d1.__setitem__(k, first_word.count(k)) for k in first_word if k != ' ']
	[d2.__setitem__(k, second_word.count(k)) for k in second_word if k != ' ']
	return d1 == d2


print(verify_anagrams("Programming", "Gram Ring Mop"))
