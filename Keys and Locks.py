# 看’#‘组成的形状是否在key中出现
def keys_and_locks(lock, some_key):
    # remove lines that all been 0, make the shape clear
    def remove_0(area):
        return [line for line in area if '#' in line]
    lock = remove_0(zip(*remove_0(lock.strip().splitlines())))
    some_key = remove_0(zip(*remove_0(some_key.strip().splitlines())))
    print(list(zip(*lock)))
    turn90 = zip(*some_key)
    turn180 = reversed(some_key)
    turn270 = zip(*turn180)
    print('===================')
    for i in [some_key, turn90, turn180, turn270]:
        print(list(i))
    return lock in [list(i) for i in [some_key, turn90, turn180, turn270]]


if __name__ == '__main__':
    print(keys_and_locks("\n0000\n00#0\n00#0\n00##\n00#0", "\n00000\n000#0\n0####\n00000\n00000"))
