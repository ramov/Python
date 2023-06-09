from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from culculate import *

async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    my_text = update.message.text 
    await update.message.reply_text(calc(my_text))


app = ApplicationBuilder().token("6214001213:AAGR6xZ2PUfyUcVyFLgZILZw1ieAxK95f40").build()

app.add_handler(MessageHandler(filters.TEXT, my_calc))

print('start server')
app.run_polling()