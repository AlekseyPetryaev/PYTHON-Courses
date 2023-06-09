# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

# Вариант 1 ЧЕРЕЗ РЕКУРСИЮ ( ели число простое тогода = True ,если число не простое тогда = False )

# n = int(input('Enter the number: '))


# def simple(num: int, x: int) -> int:
#     if n == 1 or n == 2:
#         return 1
#     if x == num // x + 1:
#         return num % x
#     return (0 if num % x == 0 else 1) * simple(num, x + 1)


# print(bool(simple(n, 2)))


# Ответ 
# Enter the number: 16127    ( это простое число)
# True

# Enter the number: 16128    ( это не простое число)
# False


# Вариант 2 ( если число простое тогда = True ,если число не простое тогда = False )

# def prime_number(n):
#     result = True 
#     # Проходим от 2 до половины заданного нами числа с помощью (n/2)
#     for i in range(2, int(n/2)):
#         if n % i == 0:  # Если оно делится на какоенибудь число до половины от заданного нами числа 
#             result = False  # тогда выводим False 
#     return result   # если нет тогда возврашаем 


# n = int(input("Введите число, которое вы ходите проверить является оно простым или нет: "))
# if prime_number(n):
#     print(f"Число {n} является простым")
# else:
#     print(f"Число {n} не является простым")


# Ответ
# Введите число, которое вы ходите проверить является оно простым или нет: 7
# Число 7 является простым

# Введите число, которое вы ходите проверить является оно простым или нет: 1073676287
# Число 1073676287 является простым