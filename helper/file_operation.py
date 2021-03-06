# -*- coding: utf-8 -*-
"""
操作文件辅助类
"""

import os
import codecs
import json


__author__ = 'JohnnyB0Y'


class FileOperation:

    def __init__(self):

        # py文件的当前路径
        self.current_path = os.getcwd()
        # 生成保存文件的文件夹
        self.save_path = os.getcwd() + '/generating_object_files'
        # 模板文件的文件夹
        self.file_templates_path = 'file_templates'

    # 生成文件和内容
    def write_to_file(self, file_name, content, suffixes):
        # 文件夹不存在就创建
        dir_path = self.save_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = dir_path + '/' + file_name + '.' + suffixes
        file = codecs.open(file_path, 'w', encoding='utf-8')
        file.write(content)
        file.close()

        # 输出 成功与否 、生成文件的路径
        print('-------------- ok --------------')

    # 读取 json 配置文件，并转换成 字典
    def dict_from_json_file(self, file_name, file_path):

        if '.json' not in file_name:
            file_name += '.json'

        if not file_path:
            file_path = self.current_path + '/' + self.file_templates_path + '/' + file_name

        # print(file_path)
        file = codecs.open(file_path, 'r+', encoding='utf-8')

        # 配置文件的 Dict
        info = json.loads(file.read())
        file.close()
        return info

    # 读取文本字符串
    def text_from_txt_file(self, file_name, file_path):

        if '.txt' not in file_name:
            file_name += '.txt'

        if not file_path:
            file_path = self.current_path + '/' + self.file_templates_path + '/' + file_name

        # print(file_path)
        file = codecs.open(file_path, 'r+', encoding='utf-8')

        # 获取文本字符串
        text = file.read()
        file.close()
        return text
