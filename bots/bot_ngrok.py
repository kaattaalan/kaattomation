# bot_ngrok.py
import telebot
from .utils.ngrok_utils import fetch_ngrok_public_urls


def setup(env):
    BOT_TOKEN = env.get("NGROK_BOT_TOKEN")
    allowed_usernames = set(env.get("ALLOWED_USERNAMES").split(','))

    # Initialize bot
    bot = telebot.TeleBot(BOT_TOKEN)
    #

    def check_username(message):
        return message.from_user.username in allowed_usernames

    @bot.message_handler(commands=['start', 'hello'], func=check_username)
    def handle_start_hello(message):
        bot.reply_to(message, "Hello, welcome to my bot!")

    @bot.message_handler(commands=['ngrok'], func=check_username)
    def handle_ngrok(message):
        try:
            public_urls = fetch_ngrok_public_urls()
            for url in public_urls:
                bot.send_message(message.chat.id, url)
        except Exception:
            bot.reply_to(message, "Ngrok is not running")

    @bot.message_handler(func=lambda message: check_username(message) and True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    return bot
