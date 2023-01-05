# ===== Задание 1:
# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,67 -> 13
# - 198,45 -> 27

'''
num = str(float(input('Input number: ')))
my_list = []
my_list += num
sum_num = 0
i = 0
my_list.remove('.')

while i < len(my_list):
    sum_num += int(my_list[i])
    i += 1
print(sum_num)

'''

# ===== Задание 2:
# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''
num = int(input('Input number: '))
my_list_1 = [1]
my_list_2 = [1]
i = 2

while i <= num:
    my_list_1.append(my_list_1[i-2]*i)
    my_list_2.append(f'{my_list_2[i-2]}*{i}')
    i += 1

print(my_list_1, my_list_2)

'''

# ===== Задание 3:
# Задайте список из n чисел последовательности (1 + 1/n)**n и
# выведите на экран их сумму.

# Пример:
# - Для n = 4: {1:2, 2:2.25, 3:2.37, 4:2.44}
#  Сумма = 9.06

'''
num = int(input('Input number: '))
dictionary = {}
i = 1

while i <= num:
    dictionary[i] = round((1 + 1/i)**i, 2)
    i += 1
print(f'n = {num}: {dictionary} \nСумма = {sum(dict.values(dictionary))}')

'''

# ===== Задание 4:
# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt
# в одной строке одно число.


import random

num = int(input('Input N: '))

my_lst = []
for n in range(-num, num + 1):
    my_lst.append(n)
# my_lst = [random.randrange(-num, num) for _ in range(-num, num + 1)] # Не понял условие. На всякий случай, сделал вариант со случайными числами тоже

print(my_lst)  # для удобства, вывожу список

f = open('file.txt','r')
product_numbers = 1
for line in f:
    product_numbers *= my_lst[int(line)]
    print(f'Index:{line}',end ="")
print()
print(f'Product numbers = {product_numbers}')
f.close()


# ===== Задание 5:
# Реализуйте алгоритм перемешивания списка.

'''
import random

my_lst = [1, 2, 3, 'asd', 'vt', 'nq', 34.45, 1.05]
print(my_lst)
random.shuffle(my_lst)
print(my_lst)

'''
