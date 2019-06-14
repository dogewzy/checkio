"""
[
['0', '1', '2', '3'],
['4', '5', '6', '7'],
['8', '9', '10', '11'],
['12', '13', '14', '15']
]

0 1 2 3 7 11 12 14 13 ....

"""

def solution(l):
    from operator import add, sub
    from itertools import cycle
    from collections import namedtuple
    right = len(l[0]) - 1
    left = 0
    down = len(l) - 1
    up = 0
    directions = {
        'right': right,
        'down': down,
        'left': left,
        'up': up,
    }
    # value的第一个值表示是对x坐标操作还是对y坐标操作，第二个至代表加一还是减一, 第三个代表反方向
    params = namedtuple('params', ['position', 'method', 'reverse'])
    opt = {
        'right': params(1, add, 'left'),
        'down': params(0, add, 'up'),
        'left': params(1, sub, 'right'),
        'up': params(0, sub, 'down'),
    }
    print(directions)
    walk = cycle(['right', 'down', 'left', 'up'])
    start = [0, 0]
    print(l[start[0]][start[1]])
    for direction in walk:
        if directions[direction] == 0:
            break
        while directions[direction]:
            param = opt[direction]
            start[param.position] = param.method(start[param.position], 1)
            directions[direction] -= 1
            directions[param.reverse] += 1
            print(start)
            print(directions)


solution([[1,2,3],[4,5,6]])