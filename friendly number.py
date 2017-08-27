def friendly_number(number, base=1000, decimals=0, suffix='',
					powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
	"""
	Format a number as friendly text, using common suffixes.
	"""
	from math import log, pow
	extend = pow(10, decimals)
	power_index = int(log(number * extend, base))
	power = powers[power_index]
	if decimals:
		cut_off_length = base * power_index - decimals
		str_num = str(number)[:-cut_off_length]
		if number[-cut_off_length] >= '5':
			str_num = str(int(str_num)+1)

	real = number / power
	return str(number)


if __name__ == '__main__':
	assert friendly_number(102) == '102', '102'
	assert friendly_number(10240) == '10k', '10k'
	assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
	assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
	assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'