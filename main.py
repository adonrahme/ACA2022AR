import logging, os
from re import S

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ["OAuth_Token"]
SLACK_APP_TOKEN = os.environ["very_original_token"]

littlehelper = App(token=SLACK_BOT_TOKEN)

@littlehelper.event("app_mention")
def mention_handler(body, context, payload, optinos, say, event):
        say("Hello World")
@littlehelper.event("message")
def message_handler(body, context, payload, options, say, event):
    pass

if __name__ == "__main__":
    handler = SocketModeHandler(littlehelper, SLACK_APP_TOKEN)
    handler.start()