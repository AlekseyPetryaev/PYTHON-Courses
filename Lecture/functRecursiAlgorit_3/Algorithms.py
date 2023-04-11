# Алгоритмы 

# Быстрая сортировака 

# def quick_sort(array):
#     if len(array) <=1:  # если число меньше или равно 1
#         return array    # тогда мы будим возвращать
#     else:
#         pivot = array[0] # мы создаем переменную в которую сохраняем все числа которые больше или равны
#     less = [i for i in array[1:] if i <= pivot]  #  в это массив мы складываем елементы меньше или равны 
#     greater = [i for i in array[1:] if i > pivot]  #  в это массив мы складываем елементы больше или равны
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# # # print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# Сортировка слиянием 

def merge_sort(nums):  # создаем наш список
    if len(nums) > 1:  # если наша длина больше 1 
        mid = len(nums) // 2  # делим наш список пополам  и вкладываем его в новую переменную
        left = nums[:mid]  # берем левую часть 
        right = nums[mid:]  # берем правую часть 
        merge_sort(left)   # сартеруем левую часть 
        merge_sort(right)  # сартируем правую часть
        i = j = k = 0      # создаем просто переменные 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # если правая больше 
                nums[k] = left[i]  # тогда в список кладем левую 
                i += 1
            else:            # если нет тогда 
                nums[k] = right[j]
                j += 1
            k += 1           # прикаждем заходе делаем плюс один

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1 

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1 

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)


#### [1, 1, 2, 2, 4, 5, 6, 7, 8, 9, 55]