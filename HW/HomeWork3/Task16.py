# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3 = это надо найти число 
# -> 1 и указать сколько раз оно встречается 

import random
a = [random.randint(0,6) for i in range(int(input(f'Сколько чисел будет: ')))]
x = a.count(int(input(f'Какое чисел найти: ')))
print(a)
print(f'Всего {x} раз встречается это число')