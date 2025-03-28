from get_data import get_data
from logger_config import setup_logging
from src.auth import auth_users

setup_logging()

if __name__ == '__main__':
    print(get_data())
