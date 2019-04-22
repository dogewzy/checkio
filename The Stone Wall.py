def stone_wall(wall):
    wall = [i for i in wall.split('\n') if i]
    thickness = len(wall)
    length = len(wall[0])
    result = []
    for i in range(length):
        result.append(len([wall[j][i] for j in range(thickness) if wall[j][i] == '#']))

    return result.index(min(result))


if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
