import requests
from requests import Response

from src.config import settings
from src.zabbix.zabbix import Zabbix
from src.jwt.jwt_check import check_token


@Zabbix
def get_data() -> Response:

    BEARER_TOKEN = check_token()

    headers = {
        'Authorization': BEARER_TOKEN,
        'Cookie': settings.ACW_TC_KEY
    }

    res: Response = requests.get(settings.URL_DATA, headers=headers)

    return res
