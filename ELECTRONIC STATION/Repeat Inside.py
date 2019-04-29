def repeat_inside(line: str):
    """
        first the longest repeating substring
    """
    from itertools import combinations as c
    result = ''
    length = len(line)
    repeat_items_alternative = [line[start: end] for start, end in c(range(length), 2) if end - start <= length / 2]
    for repeat_item in repeat_items_alternative:
        for repeat_times in range(2, length // len(repeat_item) + 1):
            if repeat_item * repeat_times in line and len(repeat_item * repeat_times) > len(result):
                result = repeat_item * repeat_times

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(repeat_inside('aaabbb'))
    print(repeat_inside('aabbff'))

    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    # print('"Run" is good. How is "Check"?')
