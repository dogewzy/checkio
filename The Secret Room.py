def secret_room(number):
    if number == 2 or number == 3:
        return 1
    elif number <= 10:
        return 5
    else:
        return 11



if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1  # five, four, one, three, two
    assert secret_room(3) == 2  # one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
