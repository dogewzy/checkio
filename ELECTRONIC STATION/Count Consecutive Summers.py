def count_consecutive_summers(num):
    if num == 1:
        return 1
    count = 0
    for divisor in range(1, num):
        result = num / divisor
        if (divisor % 2 == 0 and str(result).endswith('.5')) or (divisor % 2 == 1 and result == int(result)):
            if 2 * result - 1 >= divisor:
                count += 1
            else:
                break
    return count


if __name__ == '__main__':
    print("Example:")
    # print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    assert count_consecutive_summers(105) == 8
    print("Coding complete? Click 'Check' to earn cool rewards!")