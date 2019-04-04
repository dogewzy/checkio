def house(plan):
    rows = [i for i in plan.split('\n') if i]

    right = top = 0
    left = len(rows[0])
    bottom = len(rows)
    area_flag = False
    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if item == '#':
                area_flag = True
                if x < left:
                    left = x
                if x > right:
                    right = x
                if y > top:
                    top = y
                if y < bottom:
                    bottom = y
    if not area_flag:
        return 0
    return (right - left + 1) * (top - bottom + 1)

print(house('''0000
0000
0000
'''))