import logging
import os
from datetime import datetime

LOG_FILE=os.path.join("logs", f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


LOG_FILE_PATH=os.path.join(os.getcwd(),LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)



if __name__=="__main__":
    logging.info("Logging has started.")