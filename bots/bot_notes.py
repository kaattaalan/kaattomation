import telebot
import os


def setup(env):
    # Get the filename from the environment variable
    filename = env.get('NOTES_FILE', 'notes.txt')
    BOT_TOKEN = env.get("NOTE_BOT_TOKEN")
    allowed_usernames = set(env.get("ALLOWED_USERNAMES").split(','))

    def check_username(message):
        return message.from_user.username in allowed_usernames

    # Create the file if it doesn't exist
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('')

    # Create a bot object
    bot = telebot.TeleBot(BOT_TOKEN)

    # Define a function to handle the /start command

    @bot.message_handler(commands=['start'], func=check_username)
    def start(message):
        bot.reply_to(
            message, 'Hi! This bot can save notes to a file. To save a note, simply send me a message.')

    # Define a function to handle messages

    @bot.message_handler(func=lambda message: check_username(message))
    def save_note(message):
        # Get the note text from the message
        note_text = message.text

        # Open the file to append the note
        with open(filename, 'a') as file:
            file.write(note_text + '\n')

        # Send a confirmation message
        bot.reply_to(message, 'Note saved!')

    return bot
