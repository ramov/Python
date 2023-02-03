# ===== Задание 1:
# Вычислить число c заданной точностью d 

# Пример:
# - при d = 0.001, π = 3.141.    10^-1 ≤ d ≤10^-10  

'''
from math import pi

def accuracy_pi():
    d = float(input('Input the precision of Pi: '))
    
    if d % 1 == 0:
        print(f'Number Pi with precision {int(d)} равно {round(pi, int(d))}')
    else:
        d_len = len(str(d % 1)) - 2
        print(f'Number Pi with precision {d} равно {round(pi, d_len)}')

accuracy_pi() 

# '''

# ===== Задание 2:
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

'''
def prime_factors_of_a_number():
    n = int(input('Input n: '))
    new_n = n
    lst = []
    num = 2
    while new_n > 1:
        if new_n % num == 0:
            lst.append(num)
            new_n /= num
        else:
            num += 1
    print(lst)

prime_factors_of_a_number()

# '''

# ===== Задание 3:
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

'''
import Homework3 as h3

def unique_elements(lst):
    lst_2 = []
    i = 0

    while i < len(lst):
        if lst.count(lst[i]) == 1:
            lst_2.append(lst[i])
        i += 1

    return lst_2

my_lst = h3.random_list(10)
print(my_lst)
print(unique_elements(my_lst))

# '''

# ===== Задание 4:
# Задана натуральная степень k. 
# Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def random_list_of_polynomials(k):        
    i = 0        
    lst = []
    while i <= k:
        num = int(random.randint(0, 100))
        if num != 0:
            if i != 0 and i != 1:
                lst.insert(0,f'{num}x^{i} + ')
            elif i == 0:
                lst.insert(0,f'{num}')
            elif i == 1:
                lst.insert(0,f'{num}x + ')
        i += 1
    lst.append(' = 0')

    if '+' in lst[-2]:
        string = lst[-2].split()
        string.remove('+')
        lst[-2] = string[0]

    return lst


# k = int(input('Input the naturaal degree: '))
# with open('homework4.txt', 'w') as file:
#     for i in (random_list_of_polynomials(k)):
#         file.write(i)


# ===== Задание 5:
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

lst_f1 = ''
lst_f2 = ''
with open('file_1.txt', 'r') as f1:
    lst_f1 = str(*f1.readlines())
with open('file_2.txt', 'r') as f2:
    lst_f2 = str(*f2.readlines())

print(lst_f1)
print(lst_f2)

lst_f1 = lst_f1.replace(' ', '')
lst_f1 = lst_f1[:lst_f1.find('=')].split('+')
lst_f2 = lst_f2.replace(' ', '')
lst_f2 = lst_f2[:lst_f2.find('=')].split('+')
num_all = lst_f1 + lst_f2

my_dict = {}

for elem in num_all:
    if 'x' not in elem:
        key = 0
    elif '^' not in elem:
        key = 1
    else:
        key = int(elem[elem.find('^') + 1:])
        
    if key > 0:
        if key in my_dict:
            my_dict[key] += int(elem[:elem.find('x')])
        else:
            my_dict[key] = int(elem[:elem.find('x')])
    else:
        if key in my_dict:
            my_dict[0] += int(elem)
        else:
            my_dict[0] = int(elem) 

my_str = '' 
for key, value in sorted(my_dict.items(),reverse=True):
    if key == 0:
        my_str += str(value)
    elif key == 1:
        my_str += f'{value}*x + '
    else:
        my_str += f'{value}*x^{key} + '
    
my_str = my_str + ' = 0'

print(my_str)

with open('homework4.txt', 'w') as result:
    for el in (my_str):
        result.write(el)