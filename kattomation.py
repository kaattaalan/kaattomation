import glob
import importlib
import threading
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    env = os.environ

    for bot_file in glob.glob("bots/bot*.py"):
        module_name = bot_file.replace(
            "/", ".").replace("\\", ".").rstrip(".py")
        bot_module = importlib.import_module(module_name)
        bot = bot_module.setup(env)
        bot.infinity_polling()


if __name__ == "__main__":
    main()
