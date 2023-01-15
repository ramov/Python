# ===== Задача 1:
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def random_list(num):   # Перегрузил функцию лишней инфой для своего удобства,
    # что бы проще было создавать рандомные или псевдорандомные списки
    # Так как делал для себя, не делал "защиту от дурака :)"
    if type(num) == int:  # Integer
        lst_1 = []
        for _ in range(num):
            # для простоты проверки, привязал максимальное значение рандома к запрашиваемому числу.
            lst_1.append(random.randint(0, num))
        return lst_1
    elif type(num) == float:  # Floating
        lst_1 = []
        for _ in range(int(num)):
            lst_1.append(str(random.uniform(0, num)))
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

if __name__ == "__main__":  
    main()

# import Homework3 as h3    # вызов функции
# print(h3.random_list(5))

def sum_items_odd_position(lst_1):
    i = 1
    item_sum = 0
    while i <= len(lst_1) - 1:
        item_sum += lst_1[i]
        i += 2
    return item_sum

# вариант функции предложенный ревьюером:

# def sum_items_odd_position(lst_1):
#     item_sum = 0
#     for i in range(1, len(lst_1),2):
#         item_sum += lst_1[i]
#     return item_sum

# вариант решения предложенный преподавателем:

# import random as rand
# l = int(input('Введите длину списка: '))
# ls = [rand.randint(1,50) for i in range(l)]
# new_ls = ls[1:l:2]
# sum_nefw_ls = sum(new_ls)
# print(ls)
# print(new_ls)
# print(f'Сумма чисел на нечетных позициях равна: {sum_nefw_ls }')

'''
num = int(input('input a positive integer: '))
lst_1 = random_list(num)
print(lst_1)
print(sum_items_odd_position(lst_1))

# '''

# ===== Задача 2:
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def product_pairs_of_numbers(lst_1):
    i = 0
    j = -1
    size = len(lst_1) - 1
    result = []
    while i <= size:
        result += str(lst_1[i] * lst_1[j])
        i += 1
        j -= 1
        size -= 1
    return result

# вариант цикла предложенный ревьюером:

# def product_pairs_of_numbers(lst_1):
#     i = 0
#     size = len(lst_1) - 1
#     result = []
#     while i <= size:
#         result += str(lst_1[i] * lst_1[-1-i])
#         i += 1
#         size -= 1
#     return result

# Вариант предложенный преподавателем:

# from math import ceil
# a = []
# len_ls = int(input('Введите длину списка: '))
# for i in range(len_ls):
# a.append(int(input(f'Введите {i + 1} число: ')))
# print(a)
# newArr = []
# for j in range(ceil(len_ls / 2)):
# newArr.append(a[j] * a[-j - 1])
# print(newArr)

'''
num = int(input('input a positive integer: '))
lst_1 = random_list(num)
print(lst_1, end=' => ')
print(product_pairs_of_numbers(lst_1))

# '''

# ===== Задача 3:
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Целые числа не учитываются.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''
num = float(input('Input number: '))
lst1 = random_list(num)
lst2 = []

for item in lst1:
    if item % 1 != 0:
        lst2 += str(round(item % 1, 2))
        # lst2 += str(item % 1) # если нужно более точное значение
print(lst1)
print(lst2,'=>', max(lst2) - min(lst2))

# '''

# ===== Задача 4:
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Работает с целыми числами.


def conversion_to_binary_system(num):
    bi_num = ''
    num = abs(num)
    if num % 1 == 0:
        num = int(num)
        temp = (num % 2)
        num = int((num - temp) / 2)
        if num > 0:
            bi_num = str(temp) + bi_num
            bi_num = str(conversion_to_binary_system(num)) + bi_num
            return bi_num
        else:
            bi_num = str(temp) + bi_num
            return bi_num
    # else:  # хотел прописать функцию полностью, со всеми частными случаями и не используя bin(), но уж очень много времени кушает или я усложняю :)
    #     num_int = int(num)
    #     if num_int > 0:
    #         bi_num += str(f'{conversion_to_binary_system(num_int)}')
    #     num_flo = num % 1
    #     variable = 10**(len(str(num_flo) - 2))
    #     num_flo *= variable
    #     bi_num += str(f'.{conversion_to_binary_system(num_flo) / conversion_to_binary_system(variable)}')
    #     bi_num += str


'''

num = float(input('input a integer: '))
print(conversion_to_binary_system(num))

# '''

# Когда решил задачу, поискал более простые решение... Сказать что я был в шоке от простоты решения, это ничего не сказать xD

# второе решение:

'''

num = int(input('input a integer: '))
bi_num = ''
 
while num > 0:
    bi_num = str(num % 2) + bi_num
    num = num // 2
 
print(bi_num) 

'''

# ===== Задача 5:
# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


'''
def fibonacci(num):
    if num > 0:
        lst_1 = [0]
        lst_1.append(1)
        i = 1
        while i <= num - 1:
            lst_1.append(lst_1[i] + lst_1[i - 1])
            i+=1

        lst_2 = lst_1.copy()
        i = 2
        while i < len(lst_2):
            if i % 2 == 0:
                lst_2[i] *= -1
                i += 1
            else:
                i += 1
        lst_2.reverse()
        lst_2.remove(0)

        for j in lst_1:
            lst_2.append(j)
        print(lst_2)
    else:
        print('[0]')

num = int(input('input a integer: '))
fibonacci(num)

# '''