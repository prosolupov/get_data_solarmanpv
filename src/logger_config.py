from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add(
        "logs/logi.log",
        rotation="10 MB",
        retention="30 days",
        compression="zip"
    )