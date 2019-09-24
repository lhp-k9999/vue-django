# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 13:03
# @Author  : alvin
# @File    : json_field.py
# @Software: PyCharm

from django.db import models

# Create your models here.
ROOT_ID = 0


class Service(models.Model):
    name = models.CharField("服务的名称", default="", null=False, max_length=100)
    description = models.CharField("服务的描述", default="", null=False, max_length=2000)
    parent = models.IntegerField("服务的父节点", default=ROOT_ID, null=False, )
