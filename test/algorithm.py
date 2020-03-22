# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/12 19:51
@Auth ： WJJ
@File ：algorithm.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
t = 0
def func(n, a, b, c):
    """

    :param n:
    :param a:
    :param b:
    :param c:
    :return:
    """

    if n > 0:
        global t
        t+=1
        func(n-1, a, c, b)
        print("%s-->%s" % (a, c))
        func(n-1, b, a, c)

func(3, "a", "b", "c")
print(t)