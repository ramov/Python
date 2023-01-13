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
# num = int(input("input number: "))
# i = 2  
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(lst)

# '''

# ===== Задание 3:
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

'''
lst = list(map(int, input('Enter numbers separated by a space: ').split()))
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(new_lst)

# '''

# ===== Задание 4:
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

'''

import random

def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst

def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input('Input k = '))
koef = create_mn(k)
write_file(create_str(koef))

'''

# ===== Задание 5:
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.