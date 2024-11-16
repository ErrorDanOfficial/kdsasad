import os
import logging


class Settings:
    TOKEN = os.environ.get("8183252417:AAHPJ9qHLTFszgrDbtD7MKRoatfIBB_xHSY") or "8183252417:AAHPJ9qHLTFszgrDbtD7MKRoatfIBB_xHSY"
    CHAT_ID = os.environ.get("1241144839") or "1241144839"
    FILE_LOCATION = os.path.join(os.path.expanduser("~"), "ebayklein.db")
    TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=HTML&"""
    LOGGING = os.environ.get("LOGGING") or logging.ERROR
    URL_BASE = "https://www.kleinanzeigen.de"


settings = Settings()
