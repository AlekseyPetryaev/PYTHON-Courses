# Добавляем функцию ( filter )

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))  # Делим все числа на цела и там где останется 5 вывыдим их
# print(res)

# Ответ
# [15, 65, 175]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)   # Просто наш список 
res = filter(lambda x: x % 2 == 0, res)  # находим четные 
res = list(map(lambda x: (x, x**2), res))  #  к четным добовляем через запятую теже четное числа но в(квадрате)
print(res)

####
#####[(2, 4), (8, 64), (38, 1444)]