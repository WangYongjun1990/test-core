# -*- coding:utf-8 -*-

"""
File Name: `wrappers`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 13:53
"""

import functools
import time
import traceback

from flask import jsonify

from mitest.api.comm_log import logger
from mitest.utils.tools import get_host


def timer(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        logger.info('<==================== Begin call [{0}] ===================='.format(__get_full_class(self)))
        start_time = time.time()
        try:
            c = func(self, *args, **kw)
        except Exception as err:
            text = '\n'.join(['an error occured on {}'.format(get_host()), str(err), traceback.format_exc()])
            logger.error('Mitest: 系统发现未知错误 \n {traceback}'.format(traceback=text))
            # subject = 'Mitest: 系统发现未知错误'
            # try:
            #     from mitest.api.send_email import intf_send_mail
            #     from mitest.config.default import get_config
            #     config = get_config()
            #     email_to = config.EMAIL_TO
            #     intf_send_mail(email_to, subject, text)
            #     logger.info("send mail {} {} {}".format(email_to, subject, text))
            # except Exception as e:
            #     logger.error("cannot send email: {} {} {}".format(str(e), subject, text))
            c = jsonify({"code": "999", "desc": "system error"})
        end_time = time.time()
        d_time = end_time - start_time
        logger.info("==================== End call [{0}], run {1:.3}s ====================>\n"
                    .format(__get_full_class(self), d_time))
        return c

    return wrapper


def __get_full_class(obj):
    return "{0}.{1}".format(obj.__module__, obj.__class__.__name__)
