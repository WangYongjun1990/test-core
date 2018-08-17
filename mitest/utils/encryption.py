# -*- coding:utf-8 -*-

"""
File Name: `encryption`.py
Version:
Description:

Author: wangyongjun
Date: 2018/7/9 17:06
"""
import json
import sys

from mitest.utils.remoteBridge import RemoteBridge
from mitest.api.comm_log import logger


class Encryption(RemoteBridge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def map_to_sign(self, params):
        if isinstance(params, str):
            params_dict = eval(params)
        else:
            params_dict = params
        body = {
            "map_info": params_dict,
        }

        response = self.remote_http_post(self.map_to_sign_url, body)

        r_dict = json.loads(response)
        return r_dict

    def map_to_sign_common(self, params, key='wsxedc'):
        # params_dict = eval(params)
        body = {
            "secrectKey": key,
            "map_info": params,
        }

        response = self.remote_http_post(self.map_to_sign_common_url, body)

        return response

    def map_to_sign_new(self, params):
        # params_dict = eval(params)
        body = {
            "map_info": params,
        }

        response = self.remote_http_post(self.map_to_sign_url, body)
        r_dict = json.loads(response)
        return r_dict

    def map_to_sign_sdk(self, params, key="MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEAqSJu9MNgONpxbV4RxVSf0Sv44WNRHhqfp30Y1nPndB8rsF9FGLZD5Rq68v9DpgbC+W0Yl5bO6K5tDXBj5PNFqwIDAQABAkB2lTLQH0+ObPGL6aFyBhQLNtZHSDfucGIxrw7EBP1pNu3YIU3aXun8eeyyB72fW6YUdu2RikskR+sPf1m4PbJJAiEA9SA+2Z8ll56XHq9INSzl3vfBVwVovP6Gy21DU16ge0cCIQCwozJarzrnqKTA8PXxW0OoxsJK0Gs058fzrzdtFxJMfQIhANptjHPho97yu9jk+qQfyQqhnZBMyqM276iQSaEdvkV7AiA9nD61CMfIA7eroKB4Vffsh58/TyEFrA6/PY9cmp6EVQIgIg+Q61i3+WoGBk7IwXPQdxtFpUZtrk3GYQKXcxuzMBs="):
        if isinstance(params, str):
            params_dict = eval(params)
        else:
            params_dict = params
        body = {
            "secrectKey": key,
            "map_info": params_dict,
        }

        response = self.remote_http_post(self.map_to_sign_sdk_url, body)

        r_dict = json.loads(response)
        return r_dict

    def encrypt_public_key(self, plainText, publicKeyText):
        body = {
            "publicKey": publicKeyText,
            "plainText": plainText,
        }

        response = self.remote_http_post(self.encrypt_public_key_url, body)

        r_dict = json.loads(response)
        try:
            content = r_dict["content"]
        except KeyError:
            raise KeyError("调用{func_name}方法后, 解析返回内容失败, 缺少content".format(func_name=sys._getframe().f_code.co_name))

        return content

    def encryptByPublicKey(self, content, keyPair):
        body = {
            "publicKey": keyPair,
            "plainText": content,
        }

        response = self.remote_http_post(self.encrypt_public_key_url, body)

        r_dict = json.loads(response)
        try:
            content = r_dict["content"]
        except KeyError:
            raise KeyError("调用{func_name}方法后, 解析返回内容失败, 缺少content".format(func_name=sys._getframe().f_code.co_name))

        return content

    def aes(self, jsKey, text):
        body = {
            "publicKey": jsKey,
            "plainText": text,
        }

        response = self.remote_http_post(self.aes_url, body)

        r_dict = json.loads(response)
        try:
            content = r_dict["content"]
        except KeyError:
            raise KeyError("调用{func_name}方法后, 解析返回内容失败, 缺少content".format(func_name=sys._getframe().f_code.co_name))

        return content

    def encrypt(self, params_source, key="lV9pp+GXlhCTZwq+cjYHkg=="):
        body = {
            "publicKey": key,
            "plainText": params_source,
        }

        response = self.remote_http_post(self.encrypt_url, body)

        r_dict = json.loads(response)
        try:
            content = r_dict["content"]
        except KeyError:
            raise KeyError("调用{func_name}方法后, 解析返回内容失败, 缺少content".format(func_name=sys._getframe().f_code.co_name))

        return content

    def decript(self, Key, cipherText, ec=None):
        if ec:
            body = {
                "cipherText": cipherText,
                "password": Key,
                "ec": int(ec),
            }
        else:
            body = {
                "cipherText": cipherText,
                "password": Key,
            }

        # logger.info(json.dumps(body))
        # return body
        response = self.remote_http_post(self.decrypt_url, body)

        return response


if __name__ == '__main__':
    '''
    test cases
    '''
    e = Encryption()

    result = e.map_to_sign_common(json.dumps({
        "content": "13213",
        "timestamp": "1465802761723",
        "contact": "13585662222"
    }))
    print(result)