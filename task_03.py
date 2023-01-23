# Найти произведение пар чисел списка
# (парой считаем первый и последний, второй предпоследний и тд)

import os
import random as r
def clear(): return os.system('cls')


clear()


n = int(input('Введите число -> '))
num = [r.randint(-n, n) for i in range(n)]
print(num)
sum = [num[i]*num[-i-1] for i in range(n//2+n % 2)]
print(sum)
