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

API_ID = int(getenv("API_ID", "22844653"))
API_HASH = getenv("API_HASH", "9a656406da0a7a661348cd56a824f076")
BOT_TOKEN = getenv("BOT_TOKEN", "7009285082:AAEtuj2aLvlaebPQ3G0zKbU3CLWhgS3F2X8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8048617293").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ramsaranhero1:EMVwKybGR1lBF5DZ@cluster0.tst47tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002667336999")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002796162256"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "linkcents.com")
AD_API = getenv("AD_API", "dcf236d194a18677517677ac586db7ad83c084be")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
