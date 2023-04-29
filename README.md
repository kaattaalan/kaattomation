## Create an .env file in project root.
```
ENABLED_BOTS=bot_ngrok
NGROK_BOT_TOKEN=TOKEN
ALLOWED_USERNAMES=uname
NOTE_BOT_TOKEN=TOKEN
```

Add new bots to 'ENABLED_BOTS' to load them and run them. All bots must follow `bot_*.py` format.

## This requires the following packages (pip)
* glob2
* python-dotenv
* pyTelegrambotAPI