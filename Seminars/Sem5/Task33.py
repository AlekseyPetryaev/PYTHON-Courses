# Задача №33. 

# Вариант 1
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def vasya(array):
#     array_new = array  # заводим новую переменную и приравниваем со старыми оценками 
#     maxnum = max(array)  # находим максимум элемент и присваеваем ему название макснам
#     for i in range(len(array)):  # проходим повсей длине 
#         if array[i] == maxnum:   # если какойто из элементов будет равен макснам 
#             array_new[i] = min(array)  # тогда тогда этот элемент меняем на минимальный из этого списка
#     return array_new 

# array = [1, 3, 4, 5, 2, 5, 2, 3, 5, 4]
# print(f'Петрвоначальные оценки {array}')
# print(f'Итоговые оценки {vasya(array)}')

# Ответ
# Петрвоначальные оценки [1, 3, 4, 5, 2, 5, 2, 3, 5, 4]
# Итоговые оценки [1, 3, 4, 1, 2, 1, 2, 3, 1, 4]


# Вариант 2

# def vasya(array):
#     array_new = [0]*len(array)  # заводим новую переменную и приравниваем со старыми оценками 
#     for i in range(len(array)):  # проходим повсей длине 
#         if array[i] == max(array):   # если какойто из элементов будет равен макснам 
#             array_new[i] = min(array)  # тогда тогда этот элемент меняем на минимальный из этого списка
#         else:
#             array_new[i] = array[i]
#     return array_new 

# array = [1, 3, 4, 5, 2, 5, 2, 3, 5, 4]
# print(f'Петрвоначальные оценки {array}')
# print(f'Итоговые оценки {vasya(array)}')

# Ответ
# Петрвоначальные оценки [1, 3, 4, 5, 2, 5, 2, 3, 5, 4]
# Итоговые оценки [1, 3, 4, 1, 2, 1, 2, 3, 1, 4]

# Вариант 3 (через рекурсию)

# def min2max(nList: list, n: int, minEl: int, maxEl: int, maxIdx: int) -> list:
#     if n == len(nList):
#         nList[maxIdx] = minEl
#         return nList
#     else:
#         if minEl > nList[n]:
#             minEl = nList[n]
#         if maxEl < nList[n]:
#             maxEl = nList[n]
#             maxIdx = n
#         min2max(nList, n + 1, minEl, maxEl, maxIdx)
#         return maxEl, maxIdx
    


# nLst = [1, 2, 3, 4, 5]
# print(min2max(nLst, 0, nLst[0], nLst[0], maxIdx = 0))


# Вариант 4 (через рекурсию)

import random

def get_new_rating(rating, n, count = 0, new_rating = None):
    if new_rating is None:
        new_rating = []
    if count == n:
        return new_rating
    else:
        new_rating.append(1) if rating[count] > 4 else new_rating.append(rating[count])
    return get_new_rating(rating, n, count + 1, new_rating)

n = int(input("Введите общее количество оценки: "))
rating = [random.randint(1, 5) for _ in range(n)]
print(rating)
print(get_new_rating(rating, n))
