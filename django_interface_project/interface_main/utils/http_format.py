# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 16:55
# @Author  : alvin
# @File    : http_format.py
# @Software: PyCharm

from django.http import JsonResponse
from interface_main.exception.my_exception import ErrorCode

def response_json(success, error_code, message, data):
    '''
    定义全站返回报文格式
    :param success:    请求状态
    :param error_code: 错误码
    :param message:  消息
    :param data: 数据体
    :return:
    '''
    result = dict()
    result["success"] = success
    result["error"] = {
        "code": error_code,
        "message": message
    }
    result["data"] = data
    return JsonResponse(result, safe=False)


def response_success(data={}):
    return response_json(True, "", "", data)


def response_failed(code=ErrorCode.COMMON, message="参数错误"):
    return response_json(False, code, message, {})

