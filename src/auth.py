import requests
from loguru import logger

from src.config import settings

@logger.catch
def auth_users() -> str:
    payload = {
        'grant_type': settings.GRANT_TYPE,
        'username': settings.USER_NAME,
        'clear_text_pwd': settings.CLEAR_TEXT_PWD,
        'password': settings.PASSWORD,
        'identity_type': settings.GRANT_TYPE,
        'client_id': settings.CLIENT_ID
    }

    files={}

    headers = {
        'Content-Type': 'multipart/form-data',
    }

    response = requests.post(settings.URL_AUTH, headers=headers, data=payload, files=files)
    logger.info("Auth successful")

    print(response)
    return response.text
