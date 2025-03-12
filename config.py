# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "27066819"))
API_HASH = getenv("API_HASH", "823a68bafea9f46ab74f92656391746b")
BOT_TOKEN = getenv("BOT_TOKEN", "7884089947:AAHncP79pvuJLF5imBGl5X4BLMa6XDAKpcA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6001367891").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ramsaranhero1:EMVwKybGR1lBF5DZ@cluster0.tst47tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002387429617")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002399708847"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "2c27efcec826e037d3a3b01821da3fb0e824ded4")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
