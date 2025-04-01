from datetime import datetime, timezone
from xml.etree.ElementTree import tostring

from dotenv import dotenv_values, set_key
from loguru import logger
from pathlib import Path

from src.config import settings
from src.auth import auth_users

#env_file = Path('C:\\Users\\Users\\PycharmProjects\\get_data_solarmanpv\\.env_prod')
env_file = Path('/root/python_project/get_data_solarmanpv/.env_prod')


def check_token() -> str:
    target_date = datetime.fromtimestamp(settings.BEARER_GET_DATA, tz=timezone.utc)
    current_date = datetime.now()
    days_passed = (current_date.date() - target_date.date()).days

    if days_passed > 3:
        jwt_token = auth_users()
        set_key(env_file, "BEARER_TOKEN", f"Bearer {jwt_token}")
        set_key(env_file, "BEARER_GET_DATA", f"{current_date.timestamp()}")
        logger.info("Set new JWT token")
        return f"Bearer {jwt_token}"

    return settings.BEARER_TOKEN

