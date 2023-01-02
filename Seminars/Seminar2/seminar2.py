# my_dict = {1: 4, 2: 7, 'sdffs': 10, 4: 13, 5: 16, 6: 19}

# # 1) все ключи, уникальные
# # 2) ключами могут быть только неизменяемые типы данных
# # 3) значенииями могут быть любые типы данных
# # 4) неупорядоченные

# print(my_dict['sdffs'])
# print(my_dict[2])
# # 5) dict() - словарь
# # list() - список

# my_list = [[1, 4], [2, 7], ['sdffs', 10]]
# my_list = ([1, 4], [2, 7], ['sdffs', 10])
# my_list = [(1, 4),(2, 7), ('sdffs', 10)]
# my_list = ((1, 4),(2, 7), ('sdffs', 10))
# new_dict = dict(my_list)


# ====== Задание 1:
# Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# import os
# import random

# os.system('cls')
# n = int(input('Input number: '))

# for _ in range(n):
#     print(random.randrange(-100, 100), end=' ')

# ====== Задание 2:
# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.

# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Input number: '))
# dictionary = []
# for i in range(1, n + 1):
#     dictionary.append([i, 3 * i + 1])
# print(dict(dictionary)) # print(*dict(dictionary)) из-за * выведет все ключи.

# 2 вариант:

# n = int(input("Введите число: "))
# dict = {}
# for i in range(1, n+1):
# dict.update({i:3*i+1})
# #dict[i] = 3*i+1
# print(dict)


# 3 вариант:

# import os
# import random
# os.system('cls')

# num = int(input('Enter a number: '))
# print('num = ', num, ': {', end='')
# for i in range(num):
# print(f"{i+1}: {(i+1)*3 + 1}", end=', ')
# print('}')


# ====== Задание 3:
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# str_1 = str(input('str_1 = '))
# str_2 = str(input('str_2 = '))

# counter = str_1.count(str_2)
# print(counter)

# 2 вариант:

# str_1 = 'sdfsdfsdfxcgvhdfghsdfgsdhdfghdfghdsfgdfbs'
# str_2 = 'sdf'

# counter = 0
# for i in range(len(str_1) - len(str_2)):
#     if str_2 == str_1[i: i + len(str_2)]:
#         counter += 1

# print(f'Вторая строка встречается в первой {counter} раз')

# print(f'Вторая строка встречается в первой {counter} раз')
