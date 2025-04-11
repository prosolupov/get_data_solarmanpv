import sys
from pathlib import Path

from logger_config import setup_logging

sys.path.append(str(Path(__file__).parent.parent))

from src.get_data import get_data

setup_logging()

if __name__ == '__main__':
    get_data()
