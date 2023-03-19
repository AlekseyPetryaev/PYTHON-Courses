###### МНОЖЕСТВА 

# colors = {'red', 'green', 'dlue'}
# print(colors)  # {'red', 'green', 'dlue'}
# colors.add('red')  # через add(можем добавить что угодно)
# print(colors)  # {'red', 'green', 'dlue'}

# Ответ: ничего не поменяется так как это значение уже есть 
# {'dlue', 'red', 'green'}
# {'dlue', 'red', 'green'}

# добавляем 

# colors = {'red', 'green', 'dlue'}
# print(colors)  # {'red', 'green', 'dlue'}
# colors.add('gray')  # через add(можем добавить что угодно)
# print(colors)  # {'red', 'green', 'dlue'}

# Ответ: добавит цвет которы задали  
# {'green', 'red', 'dlue'}
# {'green', 'gray', 'red', 'dlue'}

# Удаляем 1

# colors = {'red', 'gray', 'green', 'dlue'}
# print(colors)  # {'red', 'green', 'dlue'}
# colors.remove('red')  # через remove(можем добавить что угодно)
# print(colors)  # {'red', 'green', 'dlue'}

# Ответ: удаляем цвет которы задали  
# {'dlue', 'green', 'red', 'gray'}
# {'dlue', 'green', 'gray'}

# Удаляем 2

# colors = {'red', 'gray', 'green', 'dlue'}
# print(colors)  # {'red', 'green', 'dlue'}
# colors.discard('red')  # через discard(можем добавить что угодно)
# print(colors)  # {'red', 'green', 'dlue'}

# Ответ: удаляем цвет которы задали  
# {'gray', 'red', 'green', 'dlue'}
# {'gray', 'green', 'dlue'}

# Для удаления всех элеентов из списка 

# colors = {'red', 'gray', 'green', 'dlue'}
# print(colors)  # {'red', 'green', 'dlue'}
# colors.clear()  # через discard(можем добавить что угодно)
# print(colors)  # {'red', 'green', 'dlue'}

# Ответ: удаляем цвет которы задали  
# {'gray', 'red', 'green', 'dlue'}
# set()

# замороженное множество

a = {1, 8, 6}  # присваеваем множествам значение  а

b = frozenset(a)  # присваеваем замороженное значение(а)  = b 

print(b)  # выводим

