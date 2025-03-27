import requests

from src.config import settings


def auth_users() -> str:
    payload = {
        'grant_type': settings.GRANT_TYPE,
        'username': settings.USER_NAME,
        'clear_text_pwd': settings.CLEAR_TEXT_PWD,
        'password': settings.PASSWORD,
        'identity_type': settings.GRANT_TYPE,
        'client_id': settings.CLIENT_ID
    }

    headers = {
        'Cookie': f'acw_tc={settings.ACW_TC_KEY}'
    }

    response = requests.post(settings.URL_AUTH, headers=headers, json=payload)

    print(response.text)

    return response.text
