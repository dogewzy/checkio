


def checkio(number):
    BEFORE_20 = ["", "one", "two", "three", "four", "five", "six", "seven",
                 "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
    AFTER_20 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                "eighty", "ninety"]
    if number < 20:
        return BEFORE_20[number]
    elif number < 100:
        tens, other = divmod(number, 10)
        return ' '.join([AFTER_20[tens - 2], checkio(other)]).rstrip()
    elif number < 1000:
        hundreds, other = divmod(number, 100)
        return ' '.join([checkio(hundreds), 'hundred', checkio(other)]).rstrip()

print(checkio(232))
