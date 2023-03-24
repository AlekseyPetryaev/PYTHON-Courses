# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# l = [0, -1, 5, 2, 3]


# def big_counter(list):
#     result = []
#     for i in range(len(list)-1):
#         if list[i] < list[i + 1]:
#             result.append(f'{list[i]} < {list [i + 1]}')
#     result = tuple(result)
#     print(result)


# big_counter(l)


# ('-1 < 5', '2 < 3')