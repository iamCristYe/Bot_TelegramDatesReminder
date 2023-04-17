import telebot
import os
from flask import Flask



bot = telebot.TeleBot(os.environ.get("telegram_key"))

# /start
@bot.message_handler(commands=['start'])
def _start(message):
    ## send first msg
    msg = "Hello "+str(message.chat.username)+\
          ", I'm a date reminder. Tell me birthdays and events to remind you. To learn how to use me, use \n/help"
    bot.send_message(message.chat.id, msg)

app = flask.Flask(__name__)

@app.route('/'+os.environ.get("telegram_key"), methods=['POST'])
def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
        return "!", 200

@app.route("/")
def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://bot-telegram-dates-reminder.vercel.app/"+os.environ.get("telegram_key"))
        return 'Chat with the Bot  <a href ="https://t.me/DatesReminderBot">here</a> \
          or   Check the project code <a href ="https://github.com/mdipietro09/Bot_TelegramDatesReminder">here</a>', 200
