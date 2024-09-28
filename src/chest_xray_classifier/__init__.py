# Single file for both by logging and exceptions handling

import os
import sys      # for exit function and 
import logging  

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#create logs directory if not exists
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("chest_xray_classifier") # get logger object for the project in the CWD or any other path
