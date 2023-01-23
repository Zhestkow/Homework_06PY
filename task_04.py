# Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

import os
import random as r
def clear(): return os.system('cls')

clear()

res = [(-3)**i for i in range(int(input('Введите число -> ')))]
print(res)