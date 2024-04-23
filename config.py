import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","23167322"))
API_HASH = getenv("API_HASH","9a684493404fc96d3ab58bd42a6d15eb")
BOT_TOKEN = getenv("BOT_TOKEN","")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002044251414"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1002044251414")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1002044251414"))
GCAST_USERS = list(map(int, getenv("GCAST_USERS", "5817124748 6473663036").split()))
OWNER_ID = int(getenv("OWNER_ID", 5322882174))
OWNER = int(getenv("OWNER", 5322882174))
OWNER_USERNAME = getenv("OWNER_USERNAME","koji280")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/kouji280/AnieXEricaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN",None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pixel_support92")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MONARCH_CHAT_AF")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🦋",
    "💐",
    "🧪",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/463d4310c627d380cafa0.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/ce39c4084fc9ee10e585f.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/2a6ada5925275c9942587.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://graph.org/file/227f007a732d6e5abcf63.jpg")
TELEGRAM_AUDIO_URL = "https://graph.org/file/1da5107b788b2d0cad8c8.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/c6af6e71543e8a36ec2af.jpg"
STREAM_IMG_URL = "https://graph.org/file/692d344953a9201b61e8f.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/463d4310c627d380cafa0.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/463d4310c627d380cafa0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/463d4310c627d380cafa0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/463d4310c627d380cafa0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/463d4310c627d380cafa0.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
