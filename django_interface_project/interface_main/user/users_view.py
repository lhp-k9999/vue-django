# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 9:37
# @Author  : alvin
# @File    : users_view.py
# @Software: PyCharm

from django.views.generic import View


# 一个类，继承与 View， 添加各种方法

class UserView( View ):

    def get(self, request, *args, **kwargs):
        return response_success( "get" )

    def post(self, request, *args, **kwargs):
        return response_success( "post" )

    def put(self, request, *args, **kwargs):
        return response_success( "put" )

    def patch(self, request, *args, **kwargs):
        return response_success( "patch" )

    def delete(self, request, *args, **kwargs):
        return response_success( "delete" )
