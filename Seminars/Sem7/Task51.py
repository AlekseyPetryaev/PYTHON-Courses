"""
Задача No51.Напишите функцию same_by(characteristic, objects),
которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False.
Для пустого набора объектов, функция должна возвращать True.
Аргумент characteristic - это функция, которая принимает объект и
вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
print(‘same’) else:
print(‘different’)
"""
# Ваианте 1

# def same_by(characteristic, objects) -> bool:
#     return len(set(map(characteristic, objects))) < 2


# def main() -> None:
#     values = [0, 2, 10, 6]
#     if same_by(lambda x: x % 2, values):
#         print('same')
#     else:
#         print('different')


# if __name__ == '__main__':
#     main()


# Вариант 2 

# def same_by(characteristic, objects) -> bool:
#     result = set([characteristic(obj) for obj in objects])
#     return len(result) <= 1


# if __name__ == "__main__":
#     values = [0, 2, 10, 6]
#     if same_by(lambda x: x % 2, values):
#         print('same')
#     else:
#         print('different')


# Ответ:
# same
# same



# Вариант 3

def same_by(characteristic, objects) -> bool:
    result = set()
    for odj in objects:
        spam = characteristic(odj)
        result.add(spam)
    return len(result) <= 1


if __name__ == "__main__":
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values):
        print('same')
    else:
        print('different')


# Ответ:
