def time_converter(time: str):
    if time == '12:00 a.m.':
        return "00:00"
    clock, info = time.split(' ')
    hour, minute = clock.split(':')
    if info == 'p.m.' and hour != '12':
        hour = str(int(hour) + 12)
    else:
        hour = '0' * (2 - len(hour)) + hour
    return hour + ':' + minute


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")