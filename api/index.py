from flask import Flask
import os

app = Flask(__name__)
bot = telebot.TeleBot(os.environ.get("telegram_key"))


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(
        url="https://bot-telegram-dates-reminder.vercel.app/"
        + os.environ.get("telegram_key")
    )
    return 'Chat with the Bot  <a href ="https://t.me/DatesReminderBot">here</a> or   Check the project code <a href ="https://github.com/mdipietro09/Bot_TelegramDatesReminder">here</a>'
