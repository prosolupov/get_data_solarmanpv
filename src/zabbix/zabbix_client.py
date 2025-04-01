import os

from src.config import settings

class ZabbixClient:

    host = settings.IP_ZABBIX
    hostname = "solarman"

    def send_metric(self, key: str, value: float | int):
        os.system(f"zabbix_sender -z {self.host} -s '{self.hostname}' -k {key} -o {value}")

    def send_power_metrics(self, generation: float, consumption: float, grid: float):
        self.send_metric('production', generation)
        self.send_metric('consumption', consumption)
        self.send_metric('grid', grid)


    def send_status(self, status: str, code: int):
        self.send_metric(status, code)