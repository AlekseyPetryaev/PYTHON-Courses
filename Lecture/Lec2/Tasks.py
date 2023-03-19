# Создать список чисел от 1 до 100 

# 1 Вариант 

# list_1 = []

# for i in range(1, 101):
#     list_1.append(i)

# print(list_1)

# Ответ
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
# 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
# 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
# 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
# 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# 2 Вариант

# list_1 = [i for i in range(1, 101)] 

# print(list_1)

# Ответ
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
# 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 
# 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 
# 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
# 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# 3 только четные числа 

# list_1 = [i for i in range(1, 101) if i % 2 == 0] 

# print(list_1)

# Ответ
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 
# 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 
# 94, 96, 98, 100]

# 4 только четные числа и пары к ним  

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] 

# print(list_1)

# Ответ
# [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), 
#  (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (36, 36), (38, 38), 
#  (40, 40), (42, 42), (44, 44), (46, 46), (48, 48), (50, 50), (52, 52), (54, 54), (56, 56), 
#  (58, 58), (60, 60), (62, 62), (64, 64), (66, 66), (68, 68), (70, 70), (72, 72), (74, 74), 
#  (76, 76), (78, 78), (80, 80), (82, 82), (84, 84), (86, 86), (88, 88), (90, 90), (92, 92), 
#  (94, 94), (96, 96), (98, 98), (100, 100)]

# 5 только четные числа и умножение на 2 

# list_1 = [i* 2 for i in range(1, 101) if i % 2 == 0] 

# print(list_1)

# Ответ
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 
#  100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 
#  176, 180, 184, 188, 192, 196, 200]