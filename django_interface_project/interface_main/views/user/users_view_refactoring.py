# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 9:37
# @Author  : alvin
# @File    : users_view.py
# @Software: PyCharm

from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
# from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException
from interface_main.utils.http_format import response_success


class UserView( View ):
    # 一个类，继承与 View， 添加各种方法

    def get(self, request, *args, **kwargs):
        '''
        代表登录 http://127.0.0.1:8000/api/backend/user/
        ?username=user1&password=user1
        get方法因为从url获取，所以使用request.GET.get
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        username = request.GET.get( "username" )
        password = request.GET.get( "password" )
        print( username, password )

        if "" == username or "" == password:
            raise MyException()
        if len( username ) > 50 or len( username ) < 2:
            raise MyException()
        if len( password ) > 50 or len( password ) < 2:
            raise MyException()

        res = authenticate( username=username, password=password )
        if res:
            return response_success( "登录成功" )
        else:
            raise MyException( message="登录失败" )

    def post(self, request, *args, **kwargs):
        '''
        http://127.0.0.1:8000/api/backend/users/
        post方法从boby获取，因为body返回字符串，需要解析成字典
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        body = request.body  # 返回的是字符串
        data = json.loads( body )
        print( data )
        username = data.get( "username", "" )
        password = data.get( "password", "" )

        if "" == username or "" == password:
            raise MyException()
        # db中创建用户
        res = User.objects.create_user( username=username, password=password )
        if res:
            return response_success( "注册用户成功" )
        else:
            raise MyException( message="注册失败！" )

    def put(self, request, *args, **kwargs):
        return response_success( "put" )

    def patch(self, request, *args, **kwargs):
        return response_success( "patch" )

    def delete(self, request, *args, **kwargs):
        return response_success( "delete" )
