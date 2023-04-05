# Декоратор 
from datetime import datetime
from time import sleep


def time_now(msg, *, dt=datetime.now()):
    print(msg, dt)


# Тесты
time_now('Сейчас такое время: ')
sleep(1)
time_now('Прошла секунда: ')
sleep(1)
time_now('Ничего не понимаю... ')

import time

def main(func):

    def wrapper(*args):  # создаем некую обуртку 
        start = time.time()  # присваеваем переменной начальное время 
        result = func(*args)  # Резалт равна функции с (*args)
        print('Время работы:', time.time() - start)  # тут мы выводим резницу во времени которая была  
        return result   # вызврашаем на ружу

    return wrapper

@main
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == '__main__':
    print(get_nod(10000000000000, 50000))