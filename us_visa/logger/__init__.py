import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'Desktop\MLOPS\Visa-Approval-Prediction\logs'

logs_path = os.path.join(from_root(), log_dir)

os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, LOG_FILE)

print(log_file_path)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)