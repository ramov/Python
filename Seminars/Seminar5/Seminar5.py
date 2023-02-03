# ===== Задача 35. 
# В файле находится N натуральных чисел, 
# записанных через пробел. 
# Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

'''
with open('seminar5.txt', 'r') as f1:
    data = f1.read().split()

data = list(map(int, data))

for i, el in enumerate(data[:-1]):
    if el != data[i+1] - 1:
        print(data[i+1] - 1)

# '''

'''
n = [1,2,3,4,5,6,8,9]

print(*[val for i, val in enumerate(n[1:]) if val != n[i] + 1])

# '''

# ===== Задача 36. 
# Дан список чисел. 
# Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''
my_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = list()
new_list.append(my_list[0])
counter = 0
for index in range(len(my_list)):
    if my_list[index] > new_list[counter]:
        new_list.append(my_list[index])
        counter += 1
print(new_list)

# '''

'''
my_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = list()
new_list.append(my_list[0])
print(len(new_list))

for index, elem in enumerate(my_list):
if elem > new_list[-1]:
new_list.append(elem)

print(new_list)

# '''

# ===== Задача 38. 
# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".

text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))