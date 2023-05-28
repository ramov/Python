# **Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6214001213:AAGR6xZ2PUfyUcVyFLgZILZw1ieAxK95f40").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()


# text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

# text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
# print(' '.join(text))