# ========= Задание 1:
# Напишите программу, которая принимает на вход два числа и
# проверяет, является ли одно число квадратом другого.

# a = int(input('a = '))
# b = int(input('b = '))

# if a == b*b or b == a*a:
#     print('Yes')
# else:
#     print('No')

# ========= Задача 2:
# Напишите программу, которая на вход принимает 5 чисел и
# находит максимальное из них.

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))

# list = [a,b,c,d,e]
# max = list[0]
# i = 0
# while i < len(list):
#     if max < list[i]:
#         max = list[i]
#     i += 1
# print(max)

# Дано 3-х значное число. Найдите сумму цифр числа.

# a = int(input('a = '))
# sum = 0

# if a > 99 and a < 1000:
#     while a > 0:
#         sum = sum + (a % 10)
#         a //= 10
#     print(sum)
# else:
#     print("Error! Input a three-digit number")

# Даны 2 числа. Проверить делится ли 1 число на 2.

# a = int(input('a = '))
# b = int(input('b = '))

# if b != 0:
#     if a % b == 0:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('Cannot be divided by zero')


# ====== 3.
# Напишите программу, которая будет на вход принимать число N и
# выводить числа от -N до N

# num = abs(int(input('Input number: ')))
# for i in range(-num, num + 1):
#     print(i, end=" ")

# ====== 4.
# Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.

# num = float(input("Input number: "))
# a = round(num)
# b = round(num * 10)%10

# if num == a:
#     print("No")
# else:
#     print(b)

num = int(input('Input number = '))
print((num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0)
    