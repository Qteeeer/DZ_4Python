# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

import math

def roundPi(d):
    count = len(d)
    pi = str(math.pi)
    print(pi[:count])


roundNumber = input("Укажите колличество знаков после запятой (Пример: 0.001): ")
roundPi(roundNumber)