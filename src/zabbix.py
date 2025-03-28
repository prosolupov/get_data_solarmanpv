import os

from src.get_data import get_data
from src.config import settings

class Zabbix:

    @staticmethod
    def send_message():
        os.system(f"zabbix_sender -z {settings.IP_ZABBIX} -s 'solarman' -k production -o {get_data().get('generationPower')}")
        os.system(f"zabbix_sender -z {settings.IP_ZABBIX} -s 'solarman' -k consumption -o {get_data().get('usePower')}")
        os.system(f"zabbix_sender -z {settings.IP_ZABBIX} -s 'solarman' -k grid -o {get_data().get('wirePower')}")
