# -*- coding: utf-8 -*-
import os
import codecs
import json


__author__ = 'JohnnyB0Y'


class FileOperation:

    def __init__(self):

        # py文件的当前路径
        self.current_path = os.getcwd()
        # 生成保存文件的文件夹
        self.save_path = os.getcwd() + '/GeneratingObjectFiles'

    # 生成文件和内容
    def write_to_file(self, file_name, content, suffixes):
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
        if not file_path:
            file_path = self.current_path + '/' + file_name

        file = codecs.open(file_path, 'r+', encoding='utf-8')
        # 配置文件的 Dict
        info = json.loads(file.read())
        file.close()
        return info
