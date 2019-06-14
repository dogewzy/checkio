# 需要申请很多个辅助数组
def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    # 这两个数组可以放到类里避免重复申请内存
    left = []
    right = []
    for i in l[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


# 看起来像是原地排序，其实你一切片，就创建新数组了
def quick_sort2(l):
    if len(l) <= 1:
        return l
    idx_pivot = 0
    for idx, value in enumerate(l[1:]):
        real_idx = idx + 1
        if value < l[idx_pivot]:
            # 支点值和比它小的值交换
            l[idx_pivot], l[real_idx] = l[real_idx], l[idx_pivot]
            # 支点后移
            idx_pivot += 1
            # 支点值返回支点处
            l[idx_pivot], l[real_idx] = l[real_idx], l[idx_pivot]
    print(idx_pivot)
    return quick_sort2(l[:idx_pivot]) + [l[idx_pivot]] + quick_sort2(l[idx_pivot + 1:])


# 必须要用索引才是真·原地排序，可以很直观的看到，这种方法不返回数组的，而是在原数组上操作
def quick_sort3(l):
    # 因为要用到尾部的索引，所以只能在里面再加一个函数
    def qs(l, begin, end):
        if end - begin <= 1:
            return
        idx_pivot = begin
        for idx in range(begin, end):
            if l[idx] < l[idx_pivot]:
                l[idx], l[idx_pivot] = l[idx_pivot], l[idx]
                idx_pivot += 1
                l[idx], l[idx_pivot] = l[idx_pivot], l[idx]
        qs(l, begin, idx_pivot)
        qs(l, idx_pivot + 1, end)

    qs(l, 0, len(l))
    return l


print(quick_sort3([1, 7, 5, 2, 3]))
