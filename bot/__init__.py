import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "23013644"))
    API_HASH = os.environ.get("API_HASH", "
5518def8d93dd1b60f0fb4bfced8a6da")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6718796420:AAEnHEb0DHulqw1pl4F1rKTng_l1rXdKPsc")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "okbot123_bot)
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
