# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 18:12
# @Author  : alvin
# @File    : calc.py
# @Software: PyCharm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CalcUtils:

    @classmethod
    def page_data(cls, data_list, page, size):
        paginator = Paginator(data_list, size)  # Show size contacts per page
        try:
            p = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            p = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            p = paginator.page(paginator.num_pages)

        return {
            "list": p.object_list,
            "total": len(data_list),
            "page": page,
            "size": size
        }