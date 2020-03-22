# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/12 13:10
@Auth ： WJJ
@File ：creat_instance.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
"""单例模式"""
class MySinfgleton:

    _obj = None
    _init_flg = True

    def __new__(cls, *args, **kwargs):
        if cls._obj ==None:
            cls._obj = object.__new__(cls)

        return cls._obj

    def __init__(self, name):
        if MySinfgleton._init_flg:
            print(".....")
            self.name = name
            MySinfgleton._init_flg = False

