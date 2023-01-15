with open('file.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()

# exit() #Повзоляет не выполнять код, который дальше прописан

path = 'file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()


# ФУНКЦИИ

def function_name(x):
    body line 1
    . . .
    body line n
    optional return


new file function_file.py file hello.py


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

import function_file

print(function_file.f(1))  # Целое
print(function_file.f(2.3))  # 23
print(function_file.f(28))  # None


file hello.py
import function_file as ff
print(ff.f(1)) # Целое
print(ff.f(2.3)) # 23
print(ff.f(28)) # None

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...
print(new_string(4)) # 12

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# РЕКУРСИЯ

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 40):
 list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ

t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# МНОЖЕСТВА

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}