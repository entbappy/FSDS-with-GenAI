import logging
import os

#create a logger string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder = "logs"
log_file = "logs/running_log.log"

os.makedirs(log_folder, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_file)
    ]
)

logger = logging.getLogger("mylog")




def add_number(a,b):
    out = a + b
    logger.info("Successfully executed")

    return out


num = add_number(3,4)
print(num)