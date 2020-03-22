# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/12 11:10
@Auth ： WJJ
@File ：wlog.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
import time
# 封装打印日志的装饰器
# def log(func):
#     def wrapper(*agrs, **kwargs):
#         print("before====", func.__name__)
#         temp = func(*agrs, **kwargs)
#         print("after===", func.__name__)
#         return temp
#     return wrapper

# 封装打印函数执行的时间的装饰器
def get_time(foo):
    def inner(*agrs, **kwargs):
        s_time = time.time()
        foo(*agrs, **kwargs)
        e_time = time.time()
        print("3func执行了{}秒".format(e_time - s_time))
    return inner


# 完整的装饰器
def log(foo):
    def inner(*agrs, **kwargs):
        print("{}执行了".format(foo.__name__))
        res = foo(*agrs, *kwargs)
        print("执行完毕了")
        return res
    return inner


#高阶装饰器
def out_log(text):
    def log(foo):
        def inner(*agrs, **kwargs):
            print(text)
            res = foo(*agrs, *kwargs)
            return res
        return inner
    return log

# python 中的装饰器有特殊的语法@ 语法糖
# @get_time   # => func = get_time(func)  new_func = get_time(func) func = new_func
# def func():
#     time.sleep(1)
#     print("start+++++++++")


           # f2 = log(get_time(f2))
# @log       # f2 = log(f2)
# @get_time  # => f2 = get_time(f2)
# def f2():
#     time.sleep(1)
#     print("1我是f2")
#
#
# @log
# def f3():
#     time.sleep(1)
#     print("4我是无参数的")

# @log
@out_log("wrfwetge4")
def f4(x, y):
    res = x + y
    return res

a = f4(1, 4)
print(a)