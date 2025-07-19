import logging
import os
from datetime import datetime

def setUpLogger(name="device_tool"):
    os.makedirs("logs",exist_ok=True)
    log_filename = f"logs/test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler=logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    console_handler=logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

"""
if __name__=="__main__":
    logger=setUpLogger()
    logger.info("This is a smart diagnostics cli tool")"""

