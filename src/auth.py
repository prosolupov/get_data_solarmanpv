import requests

from config import settings


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
        'Cookie': 'acw_tc=0a03969b17430973541494886e421f2654648931357e2a3931eb5725ed0d53'
    }

    response = requests.post("https://home.solarmanpv.com/mdc-eu/oauth2-s/oauth/token", headers=headers, data=payload)

    print(response.json())

    return response.text


if __name__ == '__main__':
    auth_users()
