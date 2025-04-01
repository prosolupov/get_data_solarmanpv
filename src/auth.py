import requests
from loguru import logger
from requests import Response

from src.config import settings


@logger.catch
def auth_users() -> str:
    # payload = {
    #     'grant_type': settings.GRANT_TYPE,
    #     'username': settings.USER_NAME,
    #     'clear_text_pwd': settings.CLEAR_TEXT_PWD,
    #     'password': settings.PASSWORD,
    #     'identity_type': settings.GRANT_TYPE,
    #     'client_id': settings.CLIENT_ID
    # }
    #
    # files = {}
    #
    # headers = {
    #     'User-Agent': '*',
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/json',
    #     'Host': 'home.solarmanpv.com'
    # }
    #
    # response: Response = requests.post(settings.URL_AUTH, headers=headers, data=payload, files=files, allow_redirects=True)
    #
    # print(response)
    #
    # if response.status_code != 200:
    #     logger.error(response.status_code)
    # else:
    #     logger.info("Auth successful")

    payload = {
        'grant_type': 'mdc_password',
        'username': 'info@ktkprom.com',
        'clear_text_pwd': 'Ktkprom2024+',
        'password': '27398373ad63b302ccd06da4b0f780e0c60887f114f66d6ad65dfb35ffbb0b46',
        'identity_type': '2',
        'client_id': 'test'
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
