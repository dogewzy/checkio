def longest_palindromic(text):
    from attrdict import AttrDict
    result = AttrDict(half_length=0, index=0)
    text = '#' + '#'.join(text) + '#'
    for index, _ in enumerate(text):
        half_length = 0
        for distance in range(1, min(index, len(text) - index) + 1):
            if index + distance < len(text):
                # if not equal , quiet the foo loop
                if text[index + distance] == text[index - distance]:
                    half_length += 1
                    # print(half_length, index)
                    if half_length > result.half_length:
                        result.half_length, result.index = half_length, index
                else:
                    break

    start = result.index - result.half_length
    end = result.index + result.half_length + 1
    return text[start:end].replace('#', '')


# 算法讲解 https://segmentfault.com/a/1190000003914228
print(longest_palindromic("abbacccccc"))

"""
加#的原因是，让所有的input长度都变成奇数，这样回文中点就是一个字符而不是字符的中间
code review
1
    line:5  for index, _ in enumerate(text): 直接用range就好了
"""

# checkio中的最优解是……暴力解法
from itertools import combinations as C


def longest_palindromic(text):
    subs = (text[start: end] for start, end in C(range(len(text) + 1), 2))
    return max((s for s in subs if s == s[::-1]), key=len)
