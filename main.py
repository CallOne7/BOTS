import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('For help ask in Google!')


def handle_message(update, context):
    text = str(update.message.text).lower() # this receives the text from users
    response = R.sample_responses(text) # this processes it

    update.message.reply_text(response) # this puts it back out to the user


def error(update, context):             #  function that logs the errors
    print(f"Update {update} caused error {context.error}")


def main():                             # main function
    updater = Updater(keys.API_KEY, use_context=True) # create updater that starts the bot
    dp = updater.dispatcher             # create a dispatcher

    dp.add_handler(CommandHandler("start", start_command))      # create command /start
    dp.add_handler(CommandHandler("help", help_command))       # create /help command

    dp.add_handler(MessageHandler(Filters.text, handle_message))    # launch handle_message function

    dp.add_error_handler(error)                                 # launch error function

    updater.start_polling()        # code that starts the program in ()  put a time in s 0 or empty means instantly
    updater.idle()                 # it allows bot to stay active


main()                             # calls main function  
