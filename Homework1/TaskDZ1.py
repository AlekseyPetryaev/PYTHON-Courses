# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

a = int(input("В ведите число: "))

summa = 0

while a != 0:
    b = a % 10
    summa += b
    a = a // 10   
print(summa) 
