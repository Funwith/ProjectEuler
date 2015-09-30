# -*- coding: utf-8 -*-
__author__ = 'Vietworm'


def sumFibonacci(n):
    k = []
    a, b = 1, 1
    while b < n:
        if b % 2 == 0:
            k.append(b)
        #print b,
        a, b = b, a+b
    return sum(k)