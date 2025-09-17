import os
import dotenv

dotenv.load_dotenv()

# bot informations
BOT_TOKEN = os.environ.get('7431793363:AAFxmdh4KNU-LRlBPUtRhojxl2ciCR5gT9s')
API_ID = int(os.environ.get(26770715))
API_HASH = os.environ.get(ed7c836581a2e7ce78cc442e90830976)

# chat details
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get(-1003060430634, -1002793240822,-1002524710183).split())
TO_CHATS = set(int(x) for x in os.environ.get(-1002563437306, -1002927727509).split())

# filters for auto post
FILTER_TEXT = bool(os.environ.get("FILTER_TEXT", True))
FILTER_AUDIO = bool(os.environ.get("FILTER_AUDIO", True))
FILTER_DOCUMENT = bool(os.environ.get("FILTER_DOCUMENT", True))
FILTER_PHOTO = bool(os.environ.get("FILTER_PHOTO", True))
FILTER_STICKER = bool(os.environ.get("FILTER_STICKER", True))
FILTER_VIDEO = bool(os.environ.get("FILTER_VIDEO", True))
FILTER_ANIMATION = bool(os.environ.get("FILTER_ANIMATION", True))
FILTER_VOICE = bool(os.environ.get("FILTER_VOICE", True))
FILTER_VIDEO_NOTE = bool(os.environ.get("FILTER_VIDEO_NOTE", True))
FILTER_CONTACT = bool(os.environ.get("FILTER_CONTACT", True))
FILTER_LOCATION = bool(os.environ.get("FILTER_LOCATION", True))
FILTER_VENUE = bool(os.environ.get("FILTER_VENUE", True))
FILTER_POLL = bool(os.environ.get("FILTER_POLL", True))
FILTER_GAME = bool(os.environ.get("FILTER_GAME", True))

# for forwarding
AS_FORWARD = bool(os.environ.get("AS_FORWARD", False))
REPLY_MARKUP = bool(os.environ.get("REPLY_MARKUP", False))
