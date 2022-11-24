from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello World!')


with open('token') as token:
    updater = Updater(token.read().strip())

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
