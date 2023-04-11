# Семинар 8. Работа с файлами

Задача №49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# import os
# import json


# def find_contact() -> dict:
#     pass


# def file_path(file_name='contact_list'):
#     return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


# def load_form_file():
#     path = file_path()

#     with open(path, 'r', encoding='UTF-8') as file:
#         json.load(file)


# def save_to_file(contact: dict) -> None:
#     path = file_path()

#     with open(path, 'w', encoding='UTF-8') as file:
#         json.dump(contact, file, ensure_ascii=False)


# def show_on_screen(contact: list) -> None:
#     decode_keys = dict(
#         first_name='Имя: ',
#         second_name='Фамилию: ',
#         contacts='Телефон: '
#     )
#     pretty_text = str()
#     for num, elem in enumerate(contacts, 1):
#         pretty_text += f'Контакт №{num}\n'
#         pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
#         pretty_text += '______'
#     print(pretty_text)


# def create_contact_dict():
#     pass


# def new_contact() -> dict: 

#     # контактной информации может быть больше чем телефон 
#     return dict(
#         first_name=input('Введите имя контакта:\n>>> '),
#         second_name=input('Введите фамилию контакта:\n>>> '),
#         contacts=input('Введите телефон контакта:\n>>> ')
#     )


# def main() -> None:
#     contact = dict(
#         first_name='Иван',
#         second_name='Иванов',
#         contacts='123'
#     )
#     contact2 = dict(
#         first_name='Петр',
#         second_name='Петров',
#         contacts='321'
#     )
#     show_on_screen(contacts)
#     #save_to_file(contact)
#     #print(type(load_form_file()))


# if __name__ == '__main__':
#     main()

############################


import os
import json


def find_contact(contacts: list) -> None:
    what = input('Кого ищем?\n>>> ')
    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        show_on_screen(found)
    else:
        print('Никого не нашли ;(')


def file_path(file_name='contact_list'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def load_from_file():
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        json.load(file)

    return data


def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)


def show_on_screen(contacts: list) -> None:
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def create_contact_info():
    pass


def new_contact(contacts: list) -> None:
    # Контактной информации может быть больше чем только телефон
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )
    )


def menu():
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт'
    ]
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:   # 
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice


def main() -> None:
    print('Программа запущена...')
    data = load_from_file()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_contact(data)
    elif command == 2:
        new_contact(data)

    save_to_file(data)
    print('Конец программы!')


def tests():
    contact = dict(
        first_name='Иван',
        second_name='Иванов',
        contacts='123'
    )
    contact2 = dict(
        first_name='Петр',
        second_name='Петров',
        contacts='123'
    )
    contact3 = dict(
        first_name='Петр',
        second_name='Иванов',
        contacts='123'
    )
    contact4 = dict(
        first_name='Иван',
        second_name='Петров',
        contacts='123'
    )
    contacts = [contact, contact2, contact3, contact4]
    return contacts


if __name__ == '__main__':
    main()