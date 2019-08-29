# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:51
# @Author  : alvin
# @File    : my_middle_ware.py
# @Software: PyCharm

import traceback

from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin
from interface_main.utils.http_format import response_success, response_failed
from interface_main.exception.my_exception import MyException, ErrorCode

ALLOW_PATHS = ["/api/backend/user/info/", "/api/backend/users/"]


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):  # 会捕捉所有的请求
        '''
        处理所有request请求，容许的请求做用户是否登录认证校验

        除了登录的接口，其他的接口应该都是需要用户在登录过的情况才允许请求的： 这
        个就可以利用中间件来实现了 request.path 能够获取得到用户请求的path

        :param request:
        :return:
        '''
        current_path = request.path
        print("process_request-->current_path:",current_path)
        if current_path in ALLOW_PATHS:
            pass
        else:
            user = request.user
            if user.is_authenticated:  # 判断用户是否已经认证过了
                pass
            else:
                # 中间件里面是不能够抛出异常的，如果有异常的返回，必须要直接return:
                return response_failed( ErrorCode.COMMON, '用户未登录' )

                return response_failed(ErrorCode.COMMON, '用户未登录')

    def process_response(self, request, response):  # 会捕捉所有的响应
        # print('响应来了')
        return response

    def process_exception(self, request, exception):  # 会捕捉所有的异常
        # print('捕捉到异常了')
        print(traceback.print_exc())
        if isinstance(exception, MyException):
            print('这是我的错误')
            code = exception.code
            message = exception.message
            return response_failed(code, message)

        elif isinstance(exception, DatabaseError):
            print('数据库错误')
            return response_failed(ErrorCode.DB, '数据库错误')
        else:
            print('未知错误')
            return response_failed(ErrorCode.UNKNOWN, '未知错误')
