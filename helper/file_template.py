# -*- coding: utf-8 -*-


class FileTemplate:
    @staticmethod
    def oc_class_desc_text():
        text = '''//
//  $class_name.$suffixes
//
//  Created by $author on $date.
//  Copyright © $year年 $author. All rights reserved.
//'''
        return text

    @staticmethod
    def oc_class_interface_text():
        text = """@interface $class_name $type $super_class_name
$protocol_str
$property_str
$method_str
@end"""
        return text

    @staticmethod
    def oc_class_implementation_text():
        text = """@implementation $class_name
$synthesize_str
$original_method_str

#pragma mark - ----------- Getter Methods ----------
$getter_method_str
@end"""
        return text
