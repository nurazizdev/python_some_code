from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import Updater , CommandHandler

def start(update, context):
    user = update.message.from_user

    buttons = [
        [
           InlineKeyboardButton('Haqida', callbackdata='region_1') ,
           InlineKeyboardButton('Homiylar', callbackdata='region_2')
        ]
    ]

    update.message.reply_html("Assalomu alaykum <b>{}!</b>\n \n<b>SGSMS COMPANY botiga xush kelebsiz</b>".
        format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))

def main():
    updater = Updater("5045354599:AAH4140GB5B0ayTf9YX3LRRAkSzxg7ZcDl8",use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start))
    
    updater.start_polling()
    updater.idle()

main()