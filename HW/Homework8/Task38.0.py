# Создать телефонный справочник Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные, Программа должна сохранять данные в текстовом файле(txt)

# Дополнить телефонный справочник возможностью изменения и
# удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных


# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла


def show_data():
    """эта ф-ция показывает содержимое справочника"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data():
    """добавляет строку в справочник"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    

def find_data():
    """Эта ф-ция ищет информацию в справочнике"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)

def delete_person(name):
    """Удаляет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    """Изменяет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

while True:
    mode = input('Укажите цифру, команды которую хотите сделать' + '\n'
                +'0-поиск,'+'\n'+'1-чтение файла,'+'\n'+'2-добавление в файл,'+'\n'
                +'3-удаление,'+'\n'+'4-замена,'+'\n'+'5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('Такого нету, попробуйте еще')