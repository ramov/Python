# ===== Задача 38. 
# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".

'''
text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))

# '''

# ===== Задача 2:
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

'''

# Не понимаю, почему в этом варианте при выборе большего числа конфет, а потом выборе от 1 до 28, программа выдает ошибку...

import random

def toss():  # жеребьевка
    player_1 = 0
    player_2 = 0

    while player_1 == player_2:
        player_1 = random.randint(1,5)
        player_2 = random.randint(1,5)
        if player_1 > player_2:
            print('Игрок 1 берёт конфеты первый')
            break
        else:
            print('Игрок 2 берет конфеты первый')
            break

def move():  # ход игрока
    num = int(input('Введите какое кол-во конфет вы возьмете: '))
    if 0 < num < 29:
        return num
    else:
        print('Можно взять от 1 до 28 конфет')
        print()
        move()

def candy_game(candies):
    player_1 = 0
    player_2 = 0

    while candies > 0:
        print('Ходит первый игрок')
        candy = 0
        candy = move()
        player_1 += candy
        candies -= candy
        print(f'Конфет осталось = {candies}')
        print()
        if candies <= 0:
            print('Победил первый игрок')
        else:
            print('Ходит второй игрок')
            candy = 0
            candy = move()
            player_2 +=candy
            candies -= candy
            print(f'Конфет осталось = {candies}')
            print()
            if candies <= 0:
                print('Победил второй игрок')

candies = 100
toss()
candy_game(candies)

'''

# второй вариант

'''

from random import randint

candies = 2021
print(f'Всего {candies} конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        if count == 2:
            print('Ход бота')
            quantity = 20
            print(f'Бот взял {quantity} конфет')
        else:
            print('Ход бота')
            quantity = 29 - quantity
            print(f'Бот взял {quantity} конфет')
    else:
        print('Ход игрока')
        quantity = int(input('Игрок берет конфет: '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'Осталось {candies} конфет')
    else:
        print('Не жульничай! За один ход можно взять от 1 до 28 конфет!')
        count -= 1

if count % 2 == 0:
    print('Бот победил')
else:
    print('Игрок подбедил')

# '''

# ===== Задача 3: 
# Создайте программу для игры в ""Крестики-нолики"".

board = list(map(str, range(1, 10)))


def draw_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()


def place_sign(token):
    global board
    while True:
        answer = input(f"Введите число от 1 до 9.\nВыберите позицию {token}? ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                print("Эта клетка занята")
        else:
            print("Проверьте корректность ввода")


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def main():
    counter = 0
    draw_board()
    while True:
        place_sign("O") if counter % 2 else place_sign("X")
        draw_board()

        if counter > 3:
            if check_win():
                print(f"{check_win()} - победитель!")
                break
        if counter == 8:
            print("Ничья!")
            break
        counter += 1


main()

# Задача 4:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.