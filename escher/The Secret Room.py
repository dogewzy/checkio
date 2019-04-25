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


if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1  # five, four, one, three, two
    assert secret_room(3) == 2  # one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
