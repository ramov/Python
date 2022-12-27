# print('Hello world')

# value = None
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# # value = 12334
# # print(type(value))
# s = 'Hello World'

# # print(s)  # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1, 2, 3]
# list2 = ['1', '2', '3', 'Привет Мир', "Hello World", 1, 2, 4.5, True]
# print(list)
# print(list2)

# Ввод и вывод данных
# print, input

# print('Input a')
# a = input()
# print('Input b')
# b = input()
# print(a, b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# print('Input a')
# a = int(input())
# print('Input b')
# b = int(input())
# print(a, '+', b, '=', a + b)

# print('Input a')
# a = float(input())
# print('Input b')
# b = float(input())
# print(a, '+', b, '=', a + b)

# Арифметические операции
# +, -, *, /, %, //, **
# (), Сокращенные операции

# a = 1.3123
# b = 3
# c = round(a*b, 5) # где 5 указывает кол-во оставляемых знаков после запятой
# print(c)

# a = 3
# a += 5
# print(a)

# Логические операции
# a = 1 < 4 and 5 > 2
# print(a)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10 < 11 < 25 > 2 # возможно использовать большое количество сравнений
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# f = [1, 2, 3, 4]
# # print(f)
# # print(2 in f)

# is_odd = not f[0] % 2  # или f[0] % 2 == 0
# print(is_odd)

# Упровляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Input name: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print("хватит )")
# print(inverted)

# Упровляющие конструкции: for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4,10, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(4, 7):
#     print(i)

# for i in range(2, 11, 2):
#     print(i)

# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue
# for e in colors:
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')  # del colors[0] # удалить элемент

# ФУНКЦИИ


# def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return


# def f(x):
#     return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


print(f(1))  # Целое
print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneType
