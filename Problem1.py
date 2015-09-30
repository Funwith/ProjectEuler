# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

""" Có 1 dãy các số tự nhiên nhỏ hơn 10 và đó là bội của 3 hoặc 5, chúng ta tìm được các số là: 3, 5, 6 và 9.
Tổng của các bội số này là 23. Hãy tìm tổng của các bội số của 3 hoặc 5 mà nhỏ hơn 1000.
"""


def sumMultiples():
    Sum = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            Sum += i

    calc = sum([x for x in range(3, 1000) if x % 3 == 0 or x % 5 == 0])
    if Sum == calc:
        return Sum