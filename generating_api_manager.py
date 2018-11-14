# -*- coding: utf-8 -*-
"""
生成 API Manager 类文件
"""


from helper.file_operation import FileOperation
from helper.file_text import FileText


__author__ = 'JohnnyB0Y'


# 生成需要的 .h 内容
def generating_interface_file(class_name,
                              super_class_name='CTAPIBaseManager',
                              json_file_name='api_manager_pageable',
                              json_file_path=None,
                              author='JohnnyB0Y'):

    file_operation = FileOperation()
    string_list = []
    info = FileOperation().dict_from_json_file(json_file_name, json_file_path)

    # 1，拼接文件描述
    string_list.append(FileText.str_of_oc_class_desc(class_name, author, 'h'))

    # 2, 拼接 import 信息
    framework_headers = info['framework_headers']
    custom_headers = info['custom_headers']
    import_class_str = FileText.str_of_oc_import_class(framework_headers, custom_headers)

    string_list.append('\n\n')
    string_list.append(import_class_str)
    string_list.append('\n')

    # 3，拼接 interface 信息
    protocol_str = FileText.str_of_oc_protocols(info['protocols'])
    property_str = FileText.str_of_oc_properties(info['properties'])
    method_str = FileText.str_of_oc_methods(info['methods'])

    string_list.append(FileText.str_of_oc_interface(class_name,
                                                    super_class_name,
                                                    protocol_str,
                                                    True,
                                                    property_str,
                                                    method_str))
    string_list.append('\n')

    final_text = ''.join(string_list)
    file_operation.write_to_file(class_name, final_text, 'h')


# 生成需要的 .m 内容
def generating_implementation_file(class_name,
                                   json_file_name='api_manager_pageable',
                                   json_file_path=None,
                                   author='JohnnyB0Y'):

    file_operation = FileOperation()
    string_list = []
    info = FileOperation().dict_from_json_file(json_file_name, json_file_path)

    # 获取实现文件方法的字符串
    im_method_str = file_operation.text_from_txt_file('api_manager_pageable_method', None)

    # 1，拼接文件描述
    string_list.append(FileText.str_of_oc_class_desc(class_name, author, 'm'))

    # 2, 拼接 import 信息
    framework_headers = info['im_framework_headers']
    custom_headers = [class_name]
    import_class_str = FileText.str_of_oc_import_class(framework_headers, custom_headers)

    string_list.append('\n\n')
    string_list.append(import_class_str)
    string_list.append('\n')

    # 3，拼接 interface 信息
    protocol_str = FileText.str_of_oc_protocols(info['im_protocols'])
    property_str = FileText.str_of_oc_properties(info['properties'])

    string_list.append(FileText.str_of_oc_interface(class_name=class_name,
                                                    protocol_str=protocol_str,
                                                    is_category=True,
                                                    property_str=property_str))
    string_list.append('\n\n')

    # 4，拼接 implementation 信息
    string_list.append(FileText.str_of_oc_implementation(class_name, im_method_str))
    string_list.append('\n')

    final_text = ''.join(string_list)
    file_operation.write_to_file(class_name, final_text, 'm')


def generating_api_manager_file():
    prefix = input('Input all class prefix name. The default "AG": ')
    suffixes = input('Input all class suffixes name. The default "APIManager": ')
    class_name = input('Input all class middle name. Separate with an English comma ",":\n')

    if prefix == '':
        prefix = 'AG'

    if suffixes == '':
        suffixes = 'APIManager'

    # 必须输入中间名称
    if class_name == '':
        raise NameError

    class_names = class_name.split(sep=',')
    for name in class_names:
        full_class_name = prefix + name + suffixes
        generating_interface_file(full_class_name)
        generating_implementation_file(full_class_name)


# 调用
if __name__ == '__main__':
    generating_api_manager_file()
