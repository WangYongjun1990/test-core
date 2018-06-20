# -*- coding:utf-8 -*-

"""
File Name: `comm_log`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/19 17:06
"""

import logging
from logging.handlers import WatchedFileHandler
import time

from mitest.config.default import get_config

config = get_config()

log_path = config.LOG_PATH

formatter = logging.Formatter('[%(filename)-12s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')

watched_file_handler = WatchedFileHandler(log_path, encoding="utf-8")
watched_file_handler.setFormatter(formatter)

watched_file_handler.setLevel(logging.DEBUG)
# watched_file_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)

logger.addHandler(watched_file_handler)

if __name__ == "__main__":

    for i in range(10):
        logger.debug("This is debug information")
        logger.info("This is info information")
        logger.error("This is error information")
        time.sleep(.1)
