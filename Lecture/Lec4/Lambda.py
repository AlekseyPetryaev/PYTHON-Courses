# ЛЯМБДА
########(с двумя переменными) 

# def calk1(a, b):   # называем функцию 
#     return a + b  # задаем действия

# def calk2(a, b):   # называем функцию 
#     return a * b  # задаем действия

# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 45)  # 50 # можем по название цункции менять ответы


######## ЛЯМБДА  более короткая запись

# calk1 = lambda a,b: a + b  # 50

# calk2 = lambda a,b: a * b  # 225


# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 45)  # 50 # можем по название цункции менять ответы


######## ЛЯМБДА  Ещё более короткая запись

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a * b, 5, 45)  # 225
# math(lambda a,b: a + b, 5, 45)  # 50

#########################

# Задача (в списке храниться числа. Нужновыбрать только четные и составить список  число и его квадрат) 

# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# ВАРИАНТ 1

# a = [1, 2, 3, 5, 8, 15, 23, 38]
# print(a)
# b = list()

# for i in a:
#     if i % 2 == 0:           # на ходит только четные
#         b.append((i, i**2))  # записываем четное , её квадрат
        
# print(b)

# Ответ
# [1, 2, 3, 5, 8, 15, 23, 38]
# [(2, 4), (8, 64), (38, 1444)]

#  ВАРИАНТ 2 (через лямбду)

# def numbers(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = numbers(int, data)   # Просто наш список 
# print(res)
# res = where(lambda x: x % 2 == 0, res)  # находим четные 
# print(res)


# Ответ
# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]


#  ВАРИАНТ 2/1 (через лямбду)

# def numbers(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = numbers(int, data)   # Просто наш список 
# print(res)
# res = where(lambda x: x % 2 == 0, res)  # находим четные 
# print(res)
# res = list(numbers(lambda x: (x, x**2), res))  #  к четным добовляем через запятую теже четное числа но в(квадрате)
# print(res)


# Ответ
# [1, 2, 3, 5, 8, 15, 23, 38]
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)   # Просто наш список 
print(res)
res = where(lambda x: x % 2 == 0, res)  # находим четные 
print(res)
res = list(map(lambda x: (x, x**2), res))  #  к четным добовляем через запятую теже четное числа но в(квадрате)
print(res)

# Ответ
# [2, 8, 38]
# [(2, 4), (8, 64), (38, 1444)]