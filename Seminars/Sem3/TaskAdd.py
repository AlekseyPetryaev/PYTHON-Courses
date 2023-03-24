# Найти сколько раз встречается каждого элемента в масиве

# list_1 = "sghsgfhsfjsfhjsh"
# dict_2 = {}
# j = 0
# for i in list_1:
#     dict_2[i] = j 

# for i in list_1:
#     if i in dict_2:
#         dict_2[i] = dict_2[i] +1 
# print(f'Тут вы найдете, сколько встречается каждый элемент массива {dict_2}')

# Тут вы найдете, сколько встречается каждый элемент массива {'s': 5, 'g': 2, 'h': 4, 'f': 3, 'j': 2}

# вариант 2
# str1 = " a a a b c a a d c d d"

# def twin_counter(str1):
#     srt1 = str1.split(" ")
#     temp = []

#     for i in range(len(str1)):
#         counter = 0 
#         for j in str1[:i]:
#             if str1[i] == j:
#                 counter += 1
#         if counter > 0:
#             counter = f'_{counter}'  
#         else:
#             counter = ""      

#         temp.append(f'{str1[i]}{counter}')

#     print(temp)    


# twin_counter(str1)

# Вариант 3 (через словарь)

# входная строва                 и бираем пробелы
# source = 'a a a b c a a d c d d' .split()
# count_dict = {}

# def transfer(source_list: list):  # функция начинает принимать всебя список
#     for el in source_list:
#         if not count_dict.get(el):  # проверяем есть ли этот элемент в славоре 
#             count_dict[el] = 0   # в славоре нет этого элемента добавляем значение ноль 
#             yield el   # спомошью yield мы можем взять только значение 
#         count_dict[el] += 1  
#         yield f'{el}_{count_dict[el]}'

# [print(_, end=' ') for _ in transfer(source)]
# print()

# Вариант 3.1 (через словарь с индексом (idx))

# входная строва                 и бираем пробелы
# source = 'a a a b c a a d c d d' .split()
# count_dict = {}

# def transfer(source_list: list):  # функция начинает принимать всебя список
#     for idx, el in enumerate(source_list, start=1):
#         if el not in count_dict:  # проверяем есть ли этот элемент в славоре 
#             count_dict[el] = 0   # в славоре нет этого элемента добавляем значение ноль 
#             yield el   # спомошью yield мы можем взять только значение 
#             continue
#         count_dict[el] += 1  
#         yield f'{el}_{count_dict[el]}'

# [print(_, end=' ') for _ in transfer(source)]
# print()

### a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 