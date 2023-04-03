# Задача №43. 
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два 
# элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. 
# Все числа списка находятся на разных строках.

# Ввод:           Вывод:
# 1 2 3 2 3       2

# Вариант 1

# A = [1, 2, 3, 2, 3, 2]
# counter = {}

# for elem in A:
#     counter[elem] = counter.get(elem, 0) + 1

# doubles = {element: count for element, count in counter.items() if count > 1}

# print(doubles)

# Ответ
# {2: 3, 3: 3}

# Вариант 2

# A = [1, 2, 3, 2, 3, 2, 3]
# counter = {}

# from collections import Counter
# counter = Counter(A)

# package = {element: count for element, count in counter.items() if count > 1}

# print(package)

# Ответ
# {2: 3, 3: 3}

########################################
# Вариант 3

# from collections import Counter
# n = int(input("Введите количество элементов в массиве: "))
# array1 = [0]*n
# for i in range(n):
#     array1[i] = int(input("Введите элемент массива: "))
# print(f"Введенный массив: {array1}")

# c = Counter(array1)
# print(f"Количество раз, сколько встречается каждое число: {c}")

# result = 0

# def fac(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# for i in set(array1):
#     if c[i] != 1:
#         result += fac(c[i])/ (fac(c[i]-2))/ fac(2)

# print(f"Количество парных элементов равно {int(result)}")

########################################################################
# Вариает 4

# import random


# def input_num(message: str) -> int:
#     input_error: bool = True
#     while input_error:
#         try:
#             temp = int(input(message))
#         except ValueError:
#             print("Вы ввели не число!")
#         else:
#             input_error = False
#             return temp


# n = [random.randint(1, 6) for i in range(input_num('Please input size of N list: '))]
# print(n)
# l_set = set(n)
# for x in l_set:
#     if n.count(x)-1:
#         print(f' digit {x}, count - {(n.count(x) - 1)*(n.count(x)) / 2}', end=" //  ")
