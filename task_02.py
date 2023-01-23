# Найти сумму чисел списка стоящих на нечетной позиции

import os
import random as r
def clear(): return os.system('cls')


clear()


# n = int(input('Введите число -> '))
# a = [i for i in range(-5,n+1)]
a = [r.randint(-10, 10) for i in range(20) if i%2==1]
# a = list(filter(lambda x: x % 2, a))
print(f"{a}\n{sum(a)}")
