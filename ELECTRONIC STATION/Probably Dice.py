# 递归的方法还是太慢了，我不知道改如何存储之前的值，只有在target为1的时候才能返回，其实可以提前返回
def probability(dice_number, sides, target):
    if target < 1 or target > dice_number * sides:
        return 0
    if dice_number == 1:
        return 1 / sides
    else:
        return sum(
            [probability(dice_number - 1, sides, target - i) for i in range(1, sides + 1) if target - i >= 1]) / sides


def probability2(dice_number, sides, target):
    # 因为知道要算，索性先全部算好了
    from collections import namedtuple
    p = namedtuple('probability', ['dice_number', 'sides', 'target'])
    initial = {p(1, sides, i): 1/sides for i in range(1, sides)}
    for round in range(1, target // sides + 1):
        for sub_target, sub_p in {k:v for k,v in initial.items() if k.dice_number==round}:
            initial[(round+1, sides, sides+sub_target[2])] = 0


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    print(probability(2, 6, 3))
    # assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    # assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
