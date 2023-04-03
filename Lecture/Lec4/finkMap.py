# Функцыя (map)
# Название = выводим числа (от 1 до 20 )
# list_1 = [x for x in range(1, 20)]
# print(list_1)
# # к каждому значению добовляем 10
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Ответ:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

########

# Задача: C клавиатуры вводим некий набор чисел, в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки. 
# Как предварительно list строк в list чисел?

# указываем какуето строку 
# a = '15 156 96 3 5 8 52 5'
# print(a)
# #  переобразовываем строку в список 
# a = a.split()
# print(a)

# ИЛИ 
# указываем какуето строку 
a = '15 156 96 3 5 8 52 5'
print(a)
# из строки в цыфры 
# list - указываем чтобы все числа запоминались
# map - пробегаемся по всему списку 
a = list(map(int, a.split()))
print(a)


# Ответ
# 15 156 96 3 5 8 52 5
# [15, 156, 96, 3, 5, 8, 52, 5]  