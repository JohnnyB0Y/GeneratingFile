# -*- coding: utf-8 -*-


from GeneratingFileOperation import FileOperation
from GeneratingFileText import FileText


__author__ = 'JohnnyB0Y'


# 生成 VMManager oc文件
def generating_vmm_file_with_content(file_name, content, suffixes):
    file_operation = FileOperation()
    file_operation.write_to_file(file_name + 'VMManager', content, suffixes)


# 生成需要的 .h 内容
def generating_interface_file(class_name,
                              super_class_name,
                              json_file_name='VMManager',
                              json_file_path=None,
                              author='JohnnyB0Y'):

    if '.json' not in json_file_name:
        json_file_name += '.json'

    info = FileOperation().dict_from_json_file(json_file_name, json_file_path)
    string_list = []

    # 导入的协议信息
    protocols = info['protocols']

    # 导入的头文件信息
    framework_headers = info['framework_headers']
    custom_headers = info['custom_headers']
    import_class_str = FileText.import_desc_text(framework_headers, custom_headers)

    # 1，拼接文件描述
    string_list.append(FileText.class_desc_text(class_name, author, 'h'))

    # 2, 拼接 import 信息
    string_list.append('\n\n')
    string_list.append(import_class_str)
    string_list.append('\n')

    # 3，拼接 interface 信息
    string_list.append(FileText.interface_desc_text(class_name, super_class_name, protocols))
    string_list.append('\n')

    final_text = ''.join(string_list)

    print('--------------------')
    print(final_text)
    print('--------------------')

    file_operation = FileOperation()
    file_operation.write_to_file(class_name, final_text, 'h')


# 生成需要的 .m 内容
def generating_implementation_file(class_name,
                                   json_file_name='VMManager',
                                   json_file_path=None,
                                   author='JohnnyB0Y'):

    if '.json' not in json_file_name:
        json_file_name += '.json'

    info = FileOperation().dict_from_json_file(json_file_name, json_file_path)
    string_list = []

    # 导入的协议信息
    protocols = info['im_protocols']

    # 导入的头文件信息
    framework_headers = info['im_framework_headers']
    custom_headers = info['im_custom_headers']
    import_class_str = FileText.import_desc_text(framework_headers, custom_headers)

    # 1，拼接文件描述
    string_list.append(FileText.class_desc_text(class_name, author, 'm'))

    # 2, 拼接 import 信息
    string_list.append('\n\n')
    string_list.append(import_class_str)
    string_list.append('\n')

    # 3，拼接 interface 信息
    string_list.append(FileText.interface_desc_text(class_name=class_name, protocols=protocols, is_category=True))
    string_list.append('\n\n')

    # 4，拼接 implementation 信息
    string_list.append(FileText.implementation_desc_text(class_name))
    string_list.append('\n')

    final_text = ''.join(string_list)

    print('--------------------')
    print(final_text)
    print('--------------------')

    file_operation = FileOperation()
    file_operation.write_to_file(class_name, final_text, 'm')


generating_interface_file('AGBookListAPIManager', 'CTAPIBaseManager', 'VMManager')
generating_implementation_file('AGBookListAPIManager', 'VMManager')
