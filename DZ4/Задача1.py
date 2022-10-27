# Вычислить число pi c заданной точностью. 

import os
os.system('cls||clear')

from math import factorial
from decimal import *

def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    print("Потребовалось {}".format(k) +" шагов")
    return pi
    

# Требуемая точность (число знаков)
N = 100
getcontext().prec = N + 1
val = chudnovsky(N / 14)
print(val)
