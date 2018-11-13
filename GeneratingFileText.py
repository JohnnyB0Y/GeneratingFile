# -*- coding: utf-8 -*-


import time
from string import Template
from GeneratingFileTemplate import FileTemplate


class FileText:
    # 文件顶部的描述文本信息
    @staticmethod
    def class_desc_text(class_name, author, suffixes):
        # 格式化成2016-03-20 11:45:39形式
        date = time.strftime("%Y/%m/%d", time.localtime())
        year = time.strftime("%Y", time.localtime())

        # 待替换的信息
        d = {'class_name': class_name,
             'suffixes': suffixes,
             'date': date,
             'year': year,
             'author': author
             }
        return Template(FileTemplate.oc_class_desc_text()).safe_substitute(d)

    # interface 的描述文本信息
    @staticmethod
    def interface_desc_text(class_name,
                            super_class_name='',
                            protocols=None,
                            is_category=False,
                            properties=None,
                            methods=None):

        category = ':'
        if is_category:
            category = '()'

        # 导入的协议信息
        protocol_str = ''
        protocol_len = 0
        if protocols:
            protocol_len = len(protocols)

        if protocol_len > 0:
            protocol_str = '<'

        for index in range(protocol_len):
            if index < protocol_len - 1:
                protocol_str += protocols[index] + ', '
            else:
                protocol_str += protocols[index] + '>'

        # 导入的属性列表信息
        property_str = ''
        property_len = 0
        if properties:
            property_len = len(properties)

        if property_len > 0:
            property_str = '<'

        for index in range(property_len):
            if index < property_len - 1:
                property_str += properties[index] + ', '
            else:
                property_str += properties[index] + '>'

        # 导入的方法列表信息
        method_str = ''
        method_len = 0
        if methods:
            method_len = len(methods)

        if method_len > 0:
            method_str = '<'

        for index in range(method_len):
            if index < method_len - 1:
                method_str += methods[index] + ', '
            else:
                method_str += methods[index] + '>'

        # 待替换的信息
        d = {'class_name': class_name,
             'type': category,
             'super_class_name': super_class_name,
             'protocol_str': protocol_str,
             'property_str': property_str,
             'method_str': method_str,
             }
        return Template(FileTemplate.oc_class_interface_text()).safe_substitute(d)

    # implementation 的描述文本信息
    @staticmethod
    def implementation_desc_text(class_name, original_method_str='', getter_method_str='', synthesize_str=''):
        # 待替换的信息
        d = {'class_name': class_name,
             'original_method_str': original_method_str,
             'getter_method_str': getter_method_str,
             'synthesize_str': synthesize_str,
             }
        return Template(FileTemplate.oc_class_implementation_text()).safe_substitute(d)

    # 导入头文件的描述文本信息
    @staticmethod
    def import_desc_text(framework_headers=None, custom_headers=None):
        # 头文件信息
        import_class_str = ''
        for index in range(len(framework_headers)):
            import_class_str += '#import <' + framework_headers[index] + '.h>\n'

        for index in range(len(custom_headers)):
            import_class_str += '#import "' + custom_headers[index] + '.h"\n'

        return import_class_str