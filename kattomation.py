import glob
import importlib
import threading
import os
from dotenv import load_dotenv


def start_bot(env, bot_file):
    module_name = bot_file.replace("/", ".").replace("\\", ".").rstrip(".py")
    bot_module = importlib.import_module(module_name)
    bot = bot_module.setup(env)
    bot.infinity_polling()


def main():
    load_dotenv()
    env = os.environ
    enabled_bots = env.get("ENABLED_BOTS", "").split(",")
    bot_files = [f for f in glob.glob(
        "bots/bot*.py") if os.path.basename(f)[:-3] in enabled_bots]

    threads = []
    for bot_file in bot_files:
        t = threading.Thread(target=start_bot, args=(env, bot_file))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
