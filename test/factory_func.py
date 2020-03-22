# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/12 16:15
@Auth ： WJJ
@File ：factory_func.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
"""工厂函数和单例模式混用"""

class CarFactory:

    _obj = None
    _init_flg = True

    def creat_car(self, brand):

        if brand =="奔腾":
            return Benz()

        elif brand == "宝马":
            return BNW()

        elif brand == "比亚迪":
            return BYD()

        else:
            return "未知品牌, 无法创建"


    def __new__(cls, *args, **kwargs):
        if cls._obj ==None:
            cls._obj = object.__new__(cls)

        return cls._obj

    def __init__(self):
        if CarFactory._init_flg:
            print("init catfactory.....")
            CarFactory._init_flg = False
class Benz():
    pass

class BNW():
    pass

class BYD():
    pass


factory = CarFactory()
print(factory)
c1 = factory.creat_car("奔腾")
c2 = factory.creat_car("比亚迪")
print(c1)
print(c2)

factory2 = CarFactory()
print(factory2)