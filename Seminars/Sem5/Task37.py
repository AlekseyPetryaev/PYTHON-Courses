# Задача №37.

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в
# обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

# Вариант 1 
# n = [int(input('Enter the numbers: ')) for i in range(int(input('Enter the number: ')))]
# print(f'Числа введенном порядке {n}')
# n = n[::-1]
# print(f'Числа в обратном порядке {n}')

# Ответ
# Enter the number: 4
# Enter the numbers: 6
# Enter the numbers: 7
# Enter the numbers: 1
# Enter the numbers: 2
# [6, 7, 1, 2]
# [2, 1, 7, 6]

# Вариант 2 (через рекурсию)

# def input_num(message: str) -> str:
#     input_error: bool = True
#     while input_error:
#         try:
#             temp = int(input(message))
#         except ValueError:
#             print('Вы ввели не число!')
#         else:
#             input_error = False
#             return str(temp) + ' '


# def recursive_input(size_n: int):
#     if size_n == 1:
#         return [input_num('and last number: ')]
#     return [input_num('input number: ')] + recursive_input(size_n - 1)

# n = int(input('Please input number: '))

# print(*recursive_input(n)[:: - 1])

# Ответ
# Please input number: 5
# input number: 2
# input number: 3
# input number: 4
# input number: 5
# and last number: 6
# 6  5  4  3  2 


# Вариант 3 (через рекурсию)

# def recursive_input2(size_n: int):
#     x = input('please input')
#     if size_n == 1:
#         print(x, end=' ')
#     else:
#         recursive_input2(size_n - 1)
#         print(x, end=' ')


# n = int(input('please input number: '))

# recursive_input2(n)

# Ответ
# please input number: 5
# please input1
# please input5446
# please input467
# please input457
# please inputery
# ery 457 467 5446 1