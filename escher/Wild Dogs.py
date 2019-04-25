# 数学问题感觉没啥意思
def wild_dogs(coords):
    import numpy as np
    from numpy.linalg import norm
    from collections import defaultdict
    origin = np.asarray((0, 0))
    slope_with_point = defaultdict(set)
    distances = []
    for idx, coordinate1 in enumerate(coords):
        for coordinate2 in coords[idx:]:
            if coordinate1 == coordinate2:
                continue
            elif coordinate1[0] == coordinate2[0]:
                slope_with_point[(0, coordinate1[0])].update({coordinate1, coordinate2})
            else:
                slope = round((coordinate1[1] - coordinate2[1]) / (coordinate1[0] - coordinate2[0]), 2)
                x_ = round(coordinate1[0] - coordinate1[1] / slope, 0)
                slope_with_point[(slope, x_)].update({coordinate1, coordinate2})
    points = sorted(list(slope_with_point.values()), key=lambda x: len(x), reverse=True)
    min_len = len(points[0])
    for pairs in points:
        if len(pairs) == min_len:
            p1, p2 = np.asarray(pairs.pop()), np.asarray(pairs.pop())
            distances.append(norm(np.cross(p1 - origin, p2 - origin)) / norm(p2 - p1))
    distance = min(distances)
    return round(distance, 2) if int(distance) != distance else int(distance)


if __name__ == '__main__':
    print("Example:")

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print(wild_dogs([(10, 23), (4, 5), (7, 14), (10, 110)]))
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""
总结
    for idx, coordinate1 in enumerate(coords):
        for coordinate2 in coords[idx:]:
    这段代码可以用combinations实现
    
    细节上依然考虑不周，没有考虑到多组同值的情况，这里还得取一个最小值
    如果用遍历，加上最小值flag，就不会碰到这个问题，但是也会冗余的去做一些计算吧……
"""


# best solution

def wild_dogs_best(coords):
    from itertools import combinations
    result = []
    for (x0, y0), (x1, y1) in combinations(coords, 2):
        A, B, C = y0 - y1, x1 - x0, y0 * (x0 - x1) - x0 * (y0 - y1)
        distance = abs(C) / (A ** 2 + B ** 2) ** 0.5
        result += [(distance, (1, B / A, C / A) if A else (A / B, 1, C / B))]
    distance, *_ = max(result, key=lambda x: (result.count(x), -x[0]))
    return round(distance, 2)
