from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from log import *
from game_candys import *

async def not_abc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text[1:]
    items = list(filter(lambda el: 'абв' not in el.lower(), msg.split()))
    await update.message.reply_text(' '.join(items))
    await log(update, context)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text()