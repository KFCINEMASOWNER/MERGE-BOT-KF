import os


class Config(object):
    API_HASH = os.environ.get("d5850aeef7dd3d01fe6b698c0a0d4be8")
    BOT_TOKEN = os.environ.get("7541410743:AAFBFnVNU3vkcUQwvCxf-rhlnHQSUJcv_wA")
    TELEGRAM_API = os.environ.get("25953006")
    OWNER = os.environ.get("1981280736")
    OWNER_USERNAME = os.environ.get("Ask_any_Movies_1")
    PASSWORD = os.environ.get("KFCINEMAS")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("-1002237896833")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
