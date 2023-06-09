from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from random import randint, choice


# def turn_computer(candys, difficulty=False):
#     print('Ходит компьютер')
#     if difficulty:
#         computer = candys % 29
#     else:
#         computer = randint(1, 28)
#     if computer > candys:
#         computer = candys
#         print(f'Компьютер взял {computer} конфет.')
#         candys -= computer
#     return candys

# def move(candys, player, difficulty=False):
#     if player == 'игрок':
#         return turn_player(candys)
#     else:
#         return turn_computer(candys, difficulty)

# def game_bot(rest_candys, difficulty=False):
#     variants = ('игрок', 'компьютер')
#     player = choice(variants)
#     rest_candys = move(rest_candys, player, difficulty)
#     while rest_candys > 0:
#         print(f'Осталось {rest_candys} конфет')
#         player = variants[1 - variants.index(player)]
#         rest_candys = move(rest_candys, player, difficulty)
#     return player

async def turn_player(update: Update, context: ContextTypes.DEFAULT_TYPE, candys, player=''):
    await update.message.reply_text('Ходит игрок', player)
    await update.message.reply_text('Сколько конфет вы возьмёте? (1-28) :')
    take_candys = update.message.text
    if take_candys > candys:
        take_candys = candys
    candys -= take_candys
    await update.message.reply_text(f'Игрок {player} взял {take_candys} конфет.')
    await update.message.reply_text('Осталось конфет: ', candys)
    return candys

async def game_players(update: Update, context: ContextTypes.DEFAULT_TYPE, rest_candys):
    num_player = 1
    rest_candys = turn_player(rest_candys, num_player)
    while rest_candys > 0:
        await update.message.reply_text(f'Осталось {rest_candys} конфет')
        num_player = 3 - num_player
        rest_candys = turn_player(rest_candys, num_player)
    return num_player

async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Выберите вариант игры:
1 - игрок против игрока
2 - игрок против компьютера
3 - игрок против умного компьютера''')
    rest_candys = 201
    game = update.message.text[5:]
    await update.message.reply_text(game)
    if game == '1':
        result = (f'Победил {game_players(rest_candys)} игрок')
        await update.message.reply_text(result)
    # if game == '2':
    #     print(f'Победил {game_bot(rest_candys)} игрок')
    # if game == '3':
    #     print(f'Победил {game_bot(rest_candys, True)} игрок')

if __name__ == '__main__':
    main()