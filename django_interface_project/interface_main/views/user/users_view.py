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
from interface_main.forms.user import UserForm

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

        form_data = {
            "username": username,
            "password": password
        }
        form = UserForm( form_data )
        res_form = form.is_valid()
        if not res_form:
            raise MyException()
        user_auth = authenticate( username=username, password=password )
        if user_auth:
            login( request, user_auth )  # 登录持久化，生产session
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

        # form_data ={
        #     "username":username,
        #     "password":password
        # }
        # form = UserForm(form_data)
        # 类里进行参数校验
        form = UserForm( data )
        res_form = form.is_valid()
        if not res_form:
            MyException()
        # db中创建用户
        res = User.objects.create_user( username=data['username'], password=data['password'] )
        if res:
            return response_success( "注册用户成功" )
        else:
            raise MyException( message="注册失败！")


    def put(self, request, *args, **kwargs):
        return response_success( "put" )

    def patch(self, request, *args, **kwargs):
        return response_success( "patch" )

    def delete(self, request, *args, **kwargs):
        logout( request )
        return response_success( "注销成功！" )
