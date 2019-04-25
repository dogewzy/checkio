def secret_room(number):
    # 寻找递归的感觉
    table = {
        1: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
        20: ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    }

    def get_name(num):
        if num == 0:
            return ''
        if num < 20:
            return table[1][num]
        elif num < 100:
            return ' '.join([table[20][int(num / 10) - 2],  get_name(num - int(num/10)*10)]).rstrip()
        elif num < 1000:
            return ' '.join([get_name(int(num / 100)), 'hundred', get_name(num - int(num/100)*100)]).rstrip()
        else:
            return 'one thousand'

    number_list = sorted([get_name(i) for i in range(1, number + 1)])
    return number_list.index(get_name(number)) + 1

"""
可以优化的地方
1.
    table的定义可以拆分为两个变量
    BELOW_20 = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
            'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
    TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    更加清晰，命名也很好
2.
    num - int(num/100)*100这一句其实就是取余
    divmod函数可以返回商和余数，之前一直没有用过，不需要import
3.
    此外，为了更好的使用递归来计算，并且因为0不在范围内（但是我又写在数组里了），我设定num为0时返回空字符串，
    这样在join的时候就不会出问题，但其实我的rstrip已经做了这个操作了
    num为0时返回空字符串  这种操作会让人看到很奇怪
    而best solution的解决方式是在数组里把零号位置设为None，最后过滤，我觉得也比我做的好

贴一下全部代码：
BELOW_20 = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
            'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def word(nb):
    if 0 <= nb < 20:
        res = [BELOW_20[nb]]
    elif 20 <= nb < 100:
        tens, below_ten = divmod(nb, 10)
        res = [TENS[tens - 2], BELOW_20[below_ten]]
    elif 100 <= nb < 1000:
        hundreds, below_hundred = divmod(nb, 100)
        res = [BELOW_20[hundreds], 'hundred', word(below_hundred)]
    else:
        res = ['one', 'thousand']
    return ' '.join(elem for elem in res if elem) # remove possible None / 0.

secret_room = lambda door: sum(word(nb) < word(door) for nb in range(door))
"""
if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1  # five, four, one, three, two
    assert secret_room(3) == 2  # one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
