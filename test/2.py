

#快排
def QuickSort(alist, start, end):
    '''快速排序'''
    #建立递归终止条件
    if start >= end:
        return
    # low 为序列左边要移动的游标
    low = start

    # last为序列右边要移动的游标
    last = end

    # 将起始元素设为要寻找位置的基准元素
    mid_num = alist[start]

    while low < last:

        # 当low与last未重合,并且基准元素要大,就将游标向左移动
        while low < last and alist[last] >= mid_num:
            last -= 1

        #如果比基准元素小,就跳出循环,并且把其放在基准元素的左边
        alist[low] = alist[last]

        # 当low 与last 未重合,并且比基准元素要小,就将游标向右移动
        while low < last and alist[low] < mid_num:
            low += 1

        alist[last] = alist[low]

    alist[low] = mid_num

    QuickSort(alist, start, low-1) # 对左边的序列进行递归
    QuickSort(alist, low+1, end)   # 对右边序列进行递归

if __name__ == '__main__':
    alist  = [12, 25, 13, 78, 9, 5, 6, 45]

    print(alist)
    QuickSort(alist, 0, len(alist)-1)
    print(alist)


# import copy as cp
#
# i1= [1,[2,3]]
#
# i2 = cp.deepcopy(i1)
# i3 = cp.copy(i1)
#
# print(i2)
# print(i3)

from functools import wraps

def mydecorate(f):
    @wraps(f)
    def fn(*args, **kwargs):
        print('decorate called')
        return f(*args, **kwargs)

    return fn

@mydecorate
def fx():
    print('fx called')
fx()