# ======= Задача 1:
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным.

# num = int(input('Input day of week: '))
# if num > 0 and num <= 7:
#     if num == 6 or num == 7:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('There are 7 days in a week')


# ======= Задача 2:
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'¬({x} V {y} V {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
#             print(not (x or y or z) == (not x and not y and not z))


# ======= Задача 3:
# Напишите программу, которая принимает на вход координаты точки (X и Y), и
# выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# def Coordinate_Axis(x, y):
#     if x > 0 and y > 0:
#         print(1)
#     if x > 0 and y < 0:
#         print(4)
#     if x < 0 and y > 0:
#         print(2)
#     if x < 0 and y < 0:
#         print(3)

#     if x == 0 and y > 0:
#         print('0 -> Y')
#     if x == 0 and y < 0:
#         print('-Y -> 0')
#     if y == 0 and x > 0:
#         print('0 -> X')
#     if y == 0 and x < 0:
#         print('-X -> 0')

#     if x == 0 and y == 0:
#         print(0)

# x = int(input('Input X = '))
# y = int(input('Input Y = '))
# Coordinate_Axis(x, y)

# ======= Задача 4:
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# def Coordinate_Range(num):
#     if num > 0 and num <= 4:
#         if num == 1:
#             print('X = from 0 to infinity')
#             print('Y = from 0 to infinity')
#         if num == 2:
#             print('X = from 0 to minus infinity')
#             print('Y = from 0 to infinity')
#         if num == 3:
#             print('X = from 0 to minus infinity')
#             print('Y = from 0 to minus infinity')
#         if num == 4:
#             print('X = from 0 to infinity')
#             print('Y = from 0 to minus infinity')
#     else:
#         print('There are 4 quarters in the coordinate plane')

# num = int(input('Input the quarter number: '))
# Coordinate_Range(num)

# ======= Задача 5:
# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

import math

def Distance_2D():
    x1 = float(input('Input X1: '))
    y1 = float(input('Input Y1: '))
    x2 = float(input('Input X2: '))
    y2 = float(input('Input Y2: '))
    c = (int((math.sqrt((x1 - x2)**2 + (y1 - y2)**2))*100))/100
    print(c)

Distance_2D()

