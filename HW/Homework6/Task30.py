# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1, d, n = int(input('Введите число a1: ')), int(input('Введите число d: ')), int(input('Введите число n: '))
for i in range(n):
    print(a1 + i * d, end=' ')



# Ответ
# Введите число a1: 7
# Введите число d: 2
# Введите число n: 5
# 7 9 11 13 15 


# Вариант 2

a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)