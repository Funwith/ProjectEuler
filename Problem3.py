# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

import math


def isPrime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, int(math.ceil(math.sqrt(n)))):
        if n % x == 0:
            return False
        else:
            return True

