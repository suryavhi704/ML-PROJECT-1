#According to logger explanation Documentation:-
# https://docs.python.org/3/howto/logging.html
import logging
import os
from datetime import datetime

LOG_File = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_File)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)


LOG_FILE_PATH=os.path.join(os.getcwd(), "logs", LOG_File)
# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

