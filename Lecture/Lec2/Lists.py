# disctionary = {} 
# disctionary = {'up':  '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(disctionary)  # {'up':  '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(disctionary['left'])  # ←
# # типы ключей могут отличаются 
# print(disctionary['up'])   # ↑
# # типы ключей могут отличаться 
# disctionary['left']  # = ←
# print(disctionary['left'])  # = ←
# print(disctionary['type'])  # KeyError: 'type'

# {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# ←
# ↑
# ←

# добавляем к строкам цыфры

# disctionary = {} 
# disctionary = {'up':  '↑', 'left': '←', 'down': '↓', 'right': '→'}
# disctionary[895] = 98998
# print(disctionary)

# Ответ:
# {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 895: 98998}

# удаление эллента 

# del disctionary['left']  # удаление элемента
# for item in disctionary: 
    #1 print('{}: {}' .format(item, disctionary[item]))
    #2 print(item) 
#1
# up: ↑  
# down: ↓
# right: →
# 895: 98998

#2
# {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 895: 98998}
# up
# down
# right
# 895

#####

# disctionary = {} 
# disctionary = {'up':  '↑', 'left': '←', 'down': '↓', 'right': '→'}

# del disctionary['left']  # удаление элемента
# for (k,v) in disctionary.items():
#     print(k, v)

# up ↑
# down ↓
# right →

#####

# disctionary = {} 
# disctionary = {'up':  '↑', 'left': '←', 'down': '↓', 'right': '→'}

# print(disctionary.items())
# for (k,v) in disctionary.items():
#     print(k, v)   #(k) это ключ покоторому будем искать, v значение 

# dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])
# up ↑
# left ←
# down ↓
# right →
