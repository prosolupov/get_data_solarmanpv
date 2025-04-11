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
        'identity_type': settings.IDENTITY_TYPE,
        'client_id': settings.CLIENT_ID
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Cookie': 'acw_tc=0a00be9517434842566664162e432fb2d92a7b84092f8353d1d5f99293d5a4'
    }

    response = requests.post(
        settings.URL_AUTH,
        headers=headers,
        data=payload
    )

    return response.json().get("access_token")
