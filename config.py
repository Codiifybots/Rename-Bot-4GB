import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28167693")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "5924714f9a7a69c4fde389805baa7d23") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8406708945:AAEylMxwzkE8fBOGPQD1XC0aDdDQFTLk3Ew") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'codiifybots') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://gudiyakum678_db_user:4pyIIsSd8F60Fzo9@cluster0.ad5syvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Bankao")  

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "2021145517")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002521835919')) # ⚠️ Required
    DUMP_CHANNEL = int(os.environ.get('DUMP_CHANNEL', '-1002521835919'))
    
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
__**🎬 {0}**__
──────────────
**💾 Original:** __{1}__
**📦 Encoded:** __{2}__
**📉 Compression:** __{3}__
──────────────
*,⏱️ Downloaded:** __{4}__
**⏱️ Encoded:** __{5}__
**⏱️ Uploaded:** __{6}__
──────────────
"""

    dump = """
__**🎬 {0}**__
──────────────
**💾 Original:** __{1}__
**📦 Encoded:** __{2}__
**📉 Compression:** __{3}__
──────────────
*,👤 Mention:** {4}
**👤 ID:** `{5}`
──────────────
"""
