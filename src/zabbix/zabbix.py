from typing import Callable

from loguru import logger

from src.zabbix.response_validator import ResponseValidator
from src.zabbix.zabbix_client import ZabbixClient


class Zabbix:

    def __init__(self, func: Callable):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):

        self.call_count += 1
        zabbix = ZabbixClient()
        response = self.func(*args, **kwargs)
        if metrics := ResponseValidator.validate(response):
            generation, consumption, grid = metrics
            zabbix.send_power_metrics(generation, consumption, grid)
            zabbix.send_status("error", 2)
            logger.info("Metrics sent successfully")
        else:
            zabbix.send_status("error", 1)

        return response