import logging
import os
from datetime import datetime

log_dirs="logs"
os.makedirs(log_dirs,exist_ok=True)
log_file=os.path.join(log_dirs,f"logs_{datetime.now().strftime("%Y-%m-%d")}.log")

logging.basicConfig(filename=log_file,format=f"%(asctime)s - %(level)s - %(message)",level=logging.INFO)

def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
