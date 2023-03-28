# Задача 22: 

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 
# числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# from random import randint
# n = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов 1-го множества: '))))
# print(n)
# m = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов 2-го множества: '))))
# print(m)
# s_set = sorted(n.intersection(m))
# print(*s_set)



a = int(input('Введите кол-во элементов 1-го множества: '))
b = int(input('Введите кол-во элементов 2-го множества: '))

n = set(int(input('Введите элементы 1-го множества: ')) for i in range(a))
m = set(int(input('Введите элементы 2-го множества: ')) for i in range(b))
print(m)
print(n)
s_set = sorted(n.intersection(m))
print(*s_set)



####
Эталонное решения

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
# set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
# set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
# print(i, end=' ')
