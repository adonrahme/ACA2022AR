import logging
import os
import re
import pyjokes

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ["OAuth_Token"]
SLACK_APP_TOKEN = os.environ["very_original_token"]

littlehelper = App(token=SLACK_BOT_TOKEN)
logger = logging.getLogger(__name__)

@littlehelper.message(re.compile("^joke$"))
def deliverJoke(message, say):
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text=joke, channel=dm_channel)

if __name__ == "__main__":
    handler = SocketModeHandler(littlehelper, SLACK_APP_TOKEN)
    handler.start()