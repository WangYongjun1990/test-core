# -*- coding:utf-8 -*-

"""
File Name: `send_mq`.py
Version:
Description:

Author: wangyongjun
Date: 2018/8/16 14:25
"""

import json

from mitest.utils.remoteBridge import RemoteBridge
from mitest.api.comm_log import logger


class SendMQ(RemoteBridge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_mq(self, topic, tag, msg):
        """
        向远程库发送mq消息，接收返回结果
        远程接口 <remote_ip>/sendMQ
        :param topic:
        :param tag:
        :param msg:
        :return:
        """

        right_msg = self.__handle_msg(msg)
        logger.info("Format MQ入参: {}".format(right_msg))

        specific_env = self.__get_env_info()
        if not specific_env:
            return "ROBOT_ENV参数校验失败, 传入的值为{}".format(self.env)

        right_topic = self.__handle_topic(topic, specific_env)
        if not right_topic:
            return "topic参数校验失败, 传入的值为{}".format(topic)

        produce_id = self.__get_produce_id(right_topic, specific_env)
        if not produce_id:
            return "topic参数校验失败, 传入的值为{}".format(topic)

        ons_access_key = self.__get_ons_access_key(specific_env)
        if not ons_access_key:
            return "ons_access_key校验失败, 请检查PublicData文件的ons_access_key_dict"

        ons_secret_key = self.__get_ons_secret_key(specific_env)
        if not ons_secret_key:
            return "ons_secret_key校验失败, 请检查PublicData文件的ons_secret_key_dict"

        """
        input example:
        {
        "onsAccessKey": "{\"ALIUAT\":\"LTAINddRNOd9paPE\"}",
         "onsSecretKey": "{\"ALIUAT\":\"9VPymiqXViJgX1jgu3fjXuPsdAM7dL\"}",
         "topic": "TP_MIME_UNION_FINANCE",
         "tag": "TAG_FINANCE_TRANSFER_RESULT",
         "env": "ALIUAT",
         "pid": "PID_MIME_UNION_FINANCE_ALIUAT",
         "msg": "{\"loanId\":\"122342343\",\"processTime\":\"2018-04-24\",\"transferResultType\":\"DONE\"}"
         }
        """

        body = {
            "onsAccessKey": ons_access_key,
            "onsSecretKey": ons_secret_key,
            "topic": right_topic,
            "tag": tag,
            "env": specific_env,
            "pid": produce_id,
            "msg": right_msg,
        }

        # print body
        response = self.remote_http_post(self.send_mq_url, body)

        return response

    def __handle_msg(self, msg):
        if '"{"' in msg and '"}"' in msg:
            start = msg.find('"{"') + 1
            end = msg.find('"}"', start) + 2
            assert start < end
            mid = msg[start:end].replace('"', r'\"')
            return self.__handle_msg(msg[:start] + mid + msg[end:])
        else:
            return msg

    @staticmethod
    def __handle_topic(topic, specific_env):

        return topic.replace("_DEV", "").replace("_SIT", "").replace("_ALIUAT", "")

    @staticmethod
    def __get_produce_id(topic, specific_env):

        if topic.startswith("TP_"):
            produce_id = "PID_{body}_{end}".format(body=topic[3:], end=specific_env)
            return produce_id
        else:
            return ''

    def __get_ons_access_key(self, specific_env):
        try:
            value = self.ons_access_key
            ons_access_key = "{{\"{env}\":\"{value}\"}}".format(env=specific_env, value=value)
        except KeyError:
            ons_access_key = ""

        return ons_access_key

    def __get_ons_secret_key(self, specific_env):
        try:
            value = self.ons_secret_key
            ons_secret_key = "{{\"{env}\":\"{value}\"}}".format(env=specific_env, value=value)
        except KeyError:
            ons_secret_key = ""

        return ons_secret_key

    @staticmethod
    def __get_env_info():
        return "ALIUAT"


if __name__ == '__main__':
    rb = SendMQ('MOCK')

    k = rb.send_mq('TP_MIME_UNION_FINANCE',
                   'TAG_FINANCE_TRANSFER_RESULT',
                   '{"loanId":"3","processTime":"2018-04-24","transferResultType":"DONE","test":"{\"aa\":\"dsa中文\"}","test2":"{\"AA\":\"dsa中文\", \"BBB\":\"6666\"}"}',
                   # '{\"loanId\":\"122342343\",\"processTime\":\"2018-04-24\",\"transferResultType\":\"DONE\"}',
                   )
    print(k)


