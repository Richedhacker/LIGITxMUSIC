from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24513216"))
API_HASH = getenv("2079c79959648d8bbd992c4101bfcda2")

BOT_TOKEN = getenv("7533599560:AAEQt8PFmECEvlYr4ZpCyeG4Tcew1zfrreo", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7557581984"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/e6a168e4bcabd279222c1-87824a6c21a8c24055.jpg")

SESSION = getenv("1BVtsOKEBuyBpblkAxddK8W5rTn2YPY2uUpYOsHsvGAw_-mkvWcByvBtEuPwJ9xmaU69F0AEeUH8BgaskZAbunOtCvNTlLBNzMakgIIyS6LE-Qy61f7f3hbMPxxFB2VW_vSi5MdRCQuMSzIHKmfwq1-2bhIHBZd9ek0yVy4tvqJJHmMQaYhkwKb4KmQDp6JpWnY77Dmeqe9KYuqBybHSPzROfyGUj4hXcT-3CcuTgNBBsQUGz_oIiI8qOg3j73ixQnl_AmDsi7cYSGUOFsKz0NdigFvlNlAu8RgbJ7iYX04Zp1A0_XmgY_rZLPZPQAwdCnDUy1PfSHHWJO6OI6W0zWbIIn2bEmm4=", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sastatony")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/richedmod")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7170501618").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
