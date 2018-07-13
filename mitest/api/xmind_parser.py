# -*- coding:utf-8 -*-

"""
File Name: `xml_parser`.py
Version:
Description:

Author: wangyongjun
Date: 2018/7/11 9:44
"""

import os
import json
import zipfile
from collections import OrderedDict
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from mitest.api.comm_log import logger
from mitest.config.default import get_config

CONFIG = get_config()


class XmindParser(object):
    def __init__(self, **kwargs):
        self.temp_dir = CONFIG.TEMP_DIR
        self.target_xml_name = 'content.xml'
        self.xmind_file = kwargs.pop('xmind_file', None)
        self.xml_file = kwargs.pop('xml_file', None)
        self.xmlns = kwargs.pop('xmlns', '')

    def __del__(self):
        if self.xml_file:
            os.remove(self.xml_file)

    def _parse_topic(self, parent, topic):
        topic_children = topic.find(self.xmlns + 'children')
        if not topic_children:
            return
        sub_topic_list = topic_children.find(self.xmlns + 'topics').findall(self.xmlns + 'topic')
        for sub_topic in sub_topic_list:
            key = sub_topic.find(self.xmlns + 'title').text
            if key:
                parent[key] = OrderedDict()
                self._parse_topic(parent[key], sub_topic)

    def xml_to_dict(self):
        """
        解析xml，返回有序字典
        :return:
        """
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        try:
            sheet = root.find(self.xmlns+'sheet')
            topic = sheet.find(self.xmlns+'topic')
            first_topic = topic.find(self.xmlns+'title').text
        except AttributeError:
            logger.error("Incorrect XML")
            return {}
        orderd_dic = OrderedDict()
        orderd_dic[first_topic] = OrderedDict()
        self._parse_topic(orderd_dic[first_topic], topic)
        return orderd_dic

    def xmind_to_xml(self):
        """
        解压xmind，返回xml
        :return:
        """
        zfile = zipfile.ZipFile(self.xmind_file, 'r')
        print(zfile, type(zfile))
        for filename in zfile.namelist():
            print(filename, type(filename))
            if self.target_xml_name == filename:
                data = zfile.read(filename)
                with open(self.temp_dir + filename, 'w+b') as f:
                    f.write(data)

                self.xml_file = self.temp_dir + filename
                return


if __name__ == '__main__':
    kwargs = {
        "xmind_file": r"C:\Users\wangyongjun\Desktop\自动化测试平台.xmind",
        # "xml_file": r"C:\Users\wangyongjun\Desktop\content.xml",
        "xmlns": '{urn:xmind:xmap:xmlns:content:2.0}',
    }
    xp = XmindParser(**kwargs)
    xp.xmind_to_xml()
    res = xp.xml_to_dict()

    json_ = json.dumps(res, ensure_ascii=False)
    print(json_)
