# 情况是复杂又恶心
# 尝试rsplit
def safe_code(equation):
    from operator import mul, sub, truediv, add
    opt_dict = {
        '+': add,
        '*': mul,
        '-': sub
    }
    def can_startswith0(equation):
        formulation, opt, result = equation.partition('=')
        for opt_str in '+*-':
            if opt_str in formulation:
                num1, _, num2 = formulation.partition(opt_str)
        for v in [num1, num2, result]:
            if v[0] == '#':
                return False
        return True

    def value(num):
        total = 0
        num_of_sharp = 0
        if num[0] == '-':
            negative_flag = -1
            num = num[1:]
        else:
            negative_flag = 1
        for idx, number in enumerate(reversed(num)):
            if number == '#':
                num_of_sharp += 10 ** idx
            elif int(number) in range(10):
                total += 10 ** idx * int(number)
        return total * negative_flag, num_of_sharp * negative_flag
    formulation, opt, result = equation.partition('=')
    for opt_str in '+*-':
        if opt_str in formulation:
            opt = opt_dict[opt_str]
            num1, _, num2 = formulation.partition(opt_str)
            v1, sharps1 = value(num1)
            v2, sharps2 = value(num2)
            v3, sharps3 = value(result)
            for sharp in range(9):
                if str(sharp) not in equation:
                    if opt(v1 + sharps1 * sharp, v2 + sharps2 * sharp) == v3 + sharps3 * sharp:
                        if sharp == 0 and not can_startswith0(equation):
                            continue
                        return sharp
            return -1


if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")