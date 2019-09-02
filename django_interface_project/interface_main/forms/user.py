# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 18:42
# @Author  : alvin
# @File    : user.py
# @Software: PyCharm


from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=50,
                               min_length=3,
                               required=True,
                               error_messages={'required': "username can not be empty"})
    password = forms.CharField(max_length=50,
                               min_length=3,
                               required=True,
                               error_messages={'required': "password can not be empty"})

