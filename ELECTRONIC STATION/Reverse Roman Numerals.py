def reverse_roman(roman_string):
    # 把左减转化为右加
    # turn "minus at left" to "add at right" for example: IV ---> IIII
    # then we can just sum all the number in D
    # and because the "minus number length must be 1" it's easy to implement
    D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    MINUS_PAIRS = {'IV': 'IIII', 'IX': 'VIIII', 'XL': 'XXXX', 'XC': 'LXXXX', 'CD': 'CCCC', 'CM': 'DCCCC'}
    for pair in MINUS_PAIRS:
        if pair in roman_string:
            roman_string = roman_string.replace(pair, MINUS_PAIRS[pair])
    return sum([D[s] for s in roman_string])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(reverse_roman('CDXCIX'))
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    # print('Great! It is time to Check your code!')
