#Задача 14.1: ***У вас есть масив из девяти чисел составте из него максимальнон число

# a = int(input('Введите число N: '))
# list_1 = [i for i in range(1, a)]  # повазрастанию до числа n
# print(list_1)
# # list_2 = list_1[::-1]            # полный разварот массива
# # list_1.reverse()                   # полный разварот массива
# # list_1.sort(reverse=True)          # сортировка по убыванию
# s = sorted(map(str, list_1), reverse=True)
# print(s)

# n = ''
# for i in s:
#     n = n + i
# print('Искомое значение: ' + n)

# Ответ
# Введите число N: 10
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ['9', '8', '7', '6', '5', '4', '3', '2', '1']
# Искомое значение: 987654321

### Вариант через лямбду 
# 1 - (в строчку переоброзовывается, а)
# 2 - (спомошью map
# 3 - (сортировка ( ( ), по убыванию)
# 4 - (обьединяем все элементы и можем указать через что хотим = ''.join
# 5 - int() переобразовываем в число
# название функции = Лямбда аргумент(а): (4 (3 ( 2 ( 1, ), 3)))
# join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))

# if __name__ == '__main__':
#     print(join_to_biggest([501, 2, 1, 80, 9]))

# Ответ
# 98050121

### Вариант 2  через лямбду 
# 1 - (в строчку переоброзовывается, а)
# 2 - (спомошью map
# 3 - (сортировка ( ( ), по убыванию)
# 4 - (обьединяем все элементы и можем указать через что хотим = ''.join
# 5 - int() переобразовываем в число
# название функции = Лямбда аргумент(а): (4 (3 ( 2 ( 1, ), 3)))
# join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))  #  по убыванию 
# join_to_smollest = lambda a: int(''.join(sorted(map(str, a))))               #  по возростанию 

# if __name__ == '__main__':
#     print(join_to_biggest([501, 2, 1, 80, 9]))
#     print(join_to_smollest([501, 2, 1, 80, 9]))

# Ответ
# 98050121