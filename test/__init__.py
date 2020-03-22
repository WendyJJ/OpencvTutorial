# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/25 0:30
@Auth ： WJJ
@File ：__init__.py.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""


k = [1,3,2,5]
length = len(k)

for i in range(length):

    for j in range(length -1 - i):
        if k[j] > k[j+1]:
            tmp = k[j]
            k[j] = k[j+1]
            k[j+1] = tmp

            # k[j], k[j+1] = k[j+1]. k[j]

print(k)

h = [i*i for i in k]
print(h)