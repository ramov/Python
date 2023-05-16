# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from user_interface import get_data as g_d, data_import as d_i, data_export as d_e

def start():
    temp = input('Введите 1, если хотите найти или 2, если хотите добавить: ')
    if temp == 1:
        print()
    elif temp == 2:
        print()
    else:
        print('Не верный ввод, попробуйте еще раз!')
        start