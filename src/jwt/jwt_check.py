from datetime import datetime, timezone
from xml.etree.ElementTree import tostring

from dotenv import dotenv_values, set_key
from loguru import logger
from pathlib import Path
import jwt

from src.config import settings
from src.auth import auth_users

# env_file = Path('C:\\Users\\Users\\PycharmProjects\\get_data_solarmanpv\\.env_prod')
env_file = Path('/root/python_project/get_data_solarmanpv/.env_prod')


def decode_jwt() -> str:
    jwt_bearer = settings.BEARER_TOKEN.strip("Bearer")
    jwt_dec: dict = jwt.decode(jwt_bearer, options={"verify_signature": False})
    return jwt_dec.get("exp")


def check_token() -> str:

    exp_jwt: str = decode_jwt()

    target_date = datetime.fromtimestamp(exp_jwt, tz=timezone.utc)
    current_date = datetime.now()
    days_passed = (current_date.date() - target_date.date()).days

    if days_passed >= 0:
        jwt_token = auth_users()
        set_key(env_file, "BEARER_TOKEN", f"Bearer {jwt_token}")
        logger.info(f"Date exp jwt: {target_date.date()}")
        logger.info("Set new JWT token")
        return f"Bearer {jwt_token}"

    return settings.BEARER_TOKEN
