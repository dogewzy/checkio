def navigation(seaside):
    def distance(coordinate1, coordinate2):
        x1, y1 = coordinate1
        x2, y2 = coordinate2

        return max(abs(x1 - x2), abs((y1 - y2)))

    for y, row in enumerate(seaside):
        for x, item in enumerate(row):
            if item == 'Y':
                y_ = (x, y)
            elif item == 'S':
                s = (x, y)
            elif item == 'C':
                c = (x, y)
            elif item == 'M':
                m = (x, y)
    return distance(y_, s) + distance(y_, c) + distance(y_, m)

# 其实可以发现MCS部分相当冗余，改变一下思路，然后其实距离可以统一用max(abs(x1 - x2), abs((y1 - y2)))，因为其他一个为零的时候自然用另一个


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")