
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

def math(op, x, y):
    print(op(x, y))

math(lambda a,b: a * b, 5, 45)  # 225
math(lambda a,b: a + b, 5, 45)  # 50