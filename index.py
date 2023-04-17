import flask
import threading

    
import os
import telebot

app = flask.Flask(__name__)
bot = telebot.TeleBot(os.environ.get("telegram_key"))

# /start
@bot.message_handler(commands=["start"])
def _start(message):
    ## reset
    # dic_user["id"] = str(message.chat.id)
    # db.delete_one({'id':dic_user["id"]})
    # logging.info(str(message.chat.username)+" - "+str(message.chat.id)+" --- START")

    ## send first msg
    msg = (
        "Hello "
        + str(message.chat.username)
        + "我只是个倒读机"
    )
    bot.send_message(message.chat.id, msg)


# non-command message
@bot.message_handler(func=lambda m: True)
def chat(message):
    txt = message.text
    if any(x in txt.lower() for x in ["thank","thx","cool"]):
        msg = "anytime"
    elif any(x in txt.lower() for x in ["hi","hello","yo","hey"]):
        msg = "yo" if str(message.chat.username) == "none" else "yo "+str(message.chat.username)
    else:
        msg = message.text[::-1]
    bot.send_message(message.chat.id, msg)

@app.route("/" + os.environ.get("telegram_key"), methods=["POST"])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))]
    )
    return "!"


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(
        url="https://reverse-tg-bot.azurewebsites.net/"
        + os.environ.get("telegram_key")
    )
    return '倒读机'
