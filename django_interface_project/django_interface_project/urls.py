"""django_interface_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.contrib import admin
from django.urls import path

from interface_main.views.interface.interface_detail_view import InterfaceDetailView
from interface_main.views.interface.interface_list_view import InterfacesListView
from interface_main.views.user.users_view import UsersView
from interface_main.views.user.user_info_view import UserInfoView
from interface_main.views.service.service_detail_view import ServiceDetailView
from interface_main.views.service.service_list_view import ServicesListView
# http://127.0.0.1:8000/api/backend/users/ 启动成功是否测试接口

urlpatterns = [
    path('api/backend/users/', UsersView.as_view()),
    path('api/backend/user/info/', UserInfoView.as_view()),

    path('api/backend/services/', ServicesListView.as_view()),
    path('api/backend/service/<int:service_id>/', ServiceDetailView.as_view()),

    path('api/backend/interfaces/', InterfacesListView.as_view()),
    path('api/backend/interface/<int:interface_id>/', InterfaceDetailView.as_view()),
]
