import requests
from loguru import logger

from src.config import settings
from src.auth import auth_users

def get_data() -> dict:

    BEARER_TOKEN = auth_users()

    headers = {
        'Authorization': settings.BEARER_TOKEN,
        'Cookie': settings.ACW_TC_KEY
    }

    try:
        res: dict = requests.get(settings.URL_DATA, headers=headers).json()
        dict_info = {"usePower": res.get("usePower"), "wirePower": res.get("wirePower"), "generationPower": res.get("generationPower")}
        logger.info("Get info: successful")
    except:
        logger.warning("Response empty")


    return dict_info
