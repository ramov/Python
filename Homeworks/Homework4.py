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


k = int(input('Input the naturaal degree: '))
# random_list_of_polynomials(k)
with open('homework4.txt', 'w') as file:
    for i in (random_list_of_polynomials(k)):
        file.write(i)


# ===== Задание 5:
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.



