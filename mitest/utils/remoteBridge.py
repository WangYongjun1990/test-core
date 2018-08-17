# -*- coding:utf-8 -*-

"""
File Name: `remoteBridge`.py
Version:
Description:

Author: wangyongjun
Date: 2018/7/9 17:04
"""
import json
import traceback
import requests

from mitest.api.comm_log import logger
from mitest.api.mysql_manager import EnvInfoManager


class RemoteBridge(object):
    def __init__(self, **kwargs):
        env_name = kwargs.pop('env_name', None)
        dubbo_zookeeper = kwargs.pop('dubbo_zookeeper', None)
        mq_key = kwargs.pop('mq_key', None)
        remote_host = kwargs.pop('remote_host', None)

        if env_name:
            self.env = str(env_name).upper()
            obj = EnvInfoManager.env_info(self.env)[0]
            self.remote_host = obj.remote_host
            self.dubbo_zookeeper = obj.dubbo_zookeeper
            mq_key_dic = json.loads(obj.mq_key)
            self.ons_access_key = mq_key_dic['ak']
            self.ons_secret_key = mq_key_dic['sk']
        if dubbo_zookeeper:
            self.dubbo_zookeeper = dubbo_zookeeper
        if remote_host:
            self.remote_host = remote_host
        if mq_key:
            mq_key_dic = json.loads(mq_key)
            self.ons_access_key = mq_key_dic['ak']
            self.ons_secret_key = mq_key_dic['sk']

        # self.remote_host = 'http://99.48.58.177:18181'
        # self.remote_host = 'http://99.48.66.208:18181'
        # self.remote_host = 'http://99.48.58.83:18181'
        self.heard_info = {"Content-Type": "application/json;charset=UTF-8", "Connection": "close"}
        self.s = requests.session()
        self.s.keep_alive = False

        self.send_mq_url = self.remote_host + "/sendMQ"
        self.send_dubbo_url = self.remote_host + "/invokeDubbo"
        self.map_to_sign_url = self.remote_host + "/mapToSign"
        self.map_to_sign_common_url = self.remote_host + "/mapToSignCommon"
        self.map_to_sign_sdk_url = self.remote_host + "/mapToSignForSDK"
        self.encrypt_public_key_url = self.remote_host + "/encryptByPublicKey"
        self.aes_url = self.remote_host + "/encryptByAes128"
        self.encrypt_url = self.remote_host + "/encryptForKuaiMi"
        self.decrypt_url = self.remote_host + "/decryptForDataRecord"

    def remote_http_post(self, url, param):
        try:
            logger.info("============请求URL链接为============\n"
                        "{0}\n"
                        "============请求体为============\n"
                        "{1}"
                        .format(url, json.dumps(param, ensure_ascii=False, indent=4)))

            if param is not None:
                if 'Content-Type' in self.heard_info:
                    if 'application/x-www-form-urlencoded' not in self.heard_info['Content-Type']:  # 短路规则
                        param = json.dumps(param)

            try:
                response = self.s.post(url, headers=self.heard_info, data=param, verify=False, timeout=30, allow_redirects=False)
            except Exception:
                logger.info(traceback.format_exc())

            response_dict = response.json()
            # 处理status_code非200的情况
            if response.status_code != 200:
                error_msg = response_dict
                logger.error("\n============请求报错信息============"
                             "\n请求远程接口 {url} 时发生意外, 响应码={status_code}"
                             "\n详细错误: {error_msg}"
                             "\n"
                             .format(url=url,
                                     status_code=response.status_code,
                                     error_msg=error_msg))
                response.raise_for_status()

            # 处理返回报文中含remoteResponseCode字段
            if isinstance(response_dict, dict) and 'remoteResponseCode' in response_dict:
                if response_dict['remoteResponseCode'] != '000':
                    try:
                        error_msg = response_dict['content']
                    except KeyError:
                        error_msg = response_dict
                    logger.error("\n============请求报错信息============"
                                 "\n请求远程接口 {url} 时, 远程服务器返回错误信息, remoteResponseCode={remoteResponseCode}"
                                 "\n详细错误: {error_msg}"
                                 "\n"
                                 .format(url=url,
                                         remoteResponseCode=response_dict['remoteResponseCode'],
                                         error_msg=error_msg))
                    raise Exception

        except Exception:
            # logger.info(traceback.format_exc())
            raise Exception("发送Remote请求失败")

        # logger.info(response.json())
        logger.info("\n============返回消息体============"
                    "\n{}"
                    .format(json.dumps(response.json(), ensure_ascii=False, indent=4)))
        return response.text
