# from My_module import fibonacci

# print(fibonacci(5))

# My-module

# def fibonacci(num_k):
#     fib_list = [0, 1]
#     for i in range(num_k-1):
#         fib_list.append(fib_list[i]-fib_list[i+1])  # в отрицательный диапозон
#         fib_list.reverse()
#         fib_list.append(1)
#         for j in range(len(fib_list)-2, len(fib_list)-2+num_k-1):
#             fib_list.append(fib_list[j] + fib_list[j + 1])  # в положительный диапозон
#     return fib_list


# def check():
#     num = input('Введите число: ')
#     while not num.isdigit():
#         print('Введено некорректное значение! Попробуйте еще раз!')
#         num = input('Введите число: ')
#     return int(num)


# def main():
#     print('Начало старого модуля')
#     my_list = fibonacci(check())
#     print(my_list)
#     print('Конец старого модуля')


# if __name__ == "__main__":

# main()

import random

def random_list(num):   # Перегрузил функцию лишней инфой для своего удобства,
    # что бы проще было создавать рандомные или псевдорандомные списки
    # Так как делал для себя, не делал "защиту от дурака :)"
    if type(num) == int:  # Integer
        lst_1 = []
        for _ in range(num):
            # для простоты проверки, привязал максимальное значение рандома к запрашиваемому числу.
            lst_1 += str(random.randint(0, num))
        return lst_1
    elif type(num) == float:  # Floating
        lst_1 = []
        for _ in range(int(num)):
            lst_1 += str(random.uniform(0, num))
        return lst_1
    elif type(num) == str:  # String Добавил как эксперемент)))
        rand_lst = ['asda', 'sad', 'fho', 'hf', 'asfa', 'shf',
                    'o3', '4', 'hsfn', 'jh', '322', 'aSDP', 'C',
                    'V', 'W', 'E', 'T', 'U', 'WERY', 'QVBX', '[FVM]',
                    'MAV', 'UCXQW', 'UBx5', '2', '3', '4', 'qxnj',
                    'cfvSA', 'KNGBJS', '452', ';', 'BDGJD', 'LZM543GS',
                    '3245', 'jsen', 'mrbns', 'jgbns', 'jfvas',
                    'chahf', 'afvsf3', '425navva', 'lfvahfvahf',
                    'a', 'xqtmq', 'urq', 'uuq', '2u3']
        lst_1 = random.choices(rand_lst, k = int(num))
        return lst_1

# ====== Задача 1: 
# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

'''

# Вариант 1:

nums_lst = input('Input numbers = ').split()
for i in range(len(nums_lst)):
    nums_lst[i] = int(nums_lst[i])
print(max(nums_lst), ' ' ,min(nums_lst))

# Вариант 2:

nums_lst = input('Input numbers = ').split()
new_lst = []
for el in nums_lst:
    new_lst.append(int(el))
print(max(new_lst), ' ' ,min(new_lst))

# Вариант 3:

nums_lst = input('Input numbers = ').split()
max_num = int(nums_lst[0])
min_num = int(nums_lst[0])
for el in nums_lst:
    el = (int(el))
    if max_num < el:
        max_num = el
    if min_num > el:
        min_num = el
print(max_num, ' ', min_num)

'''

# nums_list = list(map(int,input().split()))

# my_list = input('Введите числа через пробел: ').split()
# print(my_list)
# num = list(map(len, my_list))

# print(num)

# num2 = [int(num) for num in input().split()]
# print(num2)


# ====== Задача 2: 
# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

'''

from math import sqrt

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

x1 = 0
x2 = 0
disc = b**2 - 4*a*c

if disc < 0:
    print('Корней нет')
elif disc == 1:
    x1 = -b/(2*a)
    print(x1)
elif disc > 0:
    x1 = (-b - sqrt(disc)) / (2 * a)
    x2 = (-b + sqrt(disc)) / (2 * a)
    print(x1, x2)

# '''

# ====== Задача 3: 
# Задайте два числа. 
# Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

number_1 = int(input("Input number 1: "))
number_2 = int(input("Input number 2: "))

max_num = max(number_1, number_2)
min_num = min(number_1, number_2)

for num in range(max_num, number_1 * number_2 + 1, max_num):
    if num % min_num  == 0:
        print(num)
        break

