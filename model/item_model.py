# -*- coding: utf-8 -*-
"""
界面选项卡模型
"""


__author__ = 'JohnnyB0Y'


class ItemModel:
    def __init__(self):
        self.property_atomic_text = ['nonatomic', 'atomic']
        self.property_assign_text = ['assign', 'strong', 'weak', 'copy']
        self.property_readonly_text = ['readonly', 'readwrite']
