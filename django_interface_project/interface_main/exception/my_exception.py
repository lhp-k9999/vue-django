# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:49
# @Author  : alvin
# @File    : my_exception.py
# @Software: PyCharm

class ErrorCode:
    DB      = 10000
    UNKNOWN = 30000
    COMMON  = 40000
    SYSTEM  = 50000


class MyException(Exception):
    def __init__(self, code=ErrorCode.COMMON, message='参数错误'):
        self.message = message
        self.code = code

    def __str__(self):
        return self.message
