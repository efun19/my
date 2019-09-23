"""test00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from userApp import views as usvv
from infomodle import  views as invv

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',usvv.indexPage),
    path('userRegist', usvv.regist),
    path('userLogin',usvv.login),
    path('uesrLogout',usvv.logout),
    path('getInfo',invv.getInfo),
    path('index2',invv.index2Page),
    path('showall',invv.list),
    path('showphoto',usvv.tuPage),
    path('photo',invv.photo),
    path('shaixuan',usvv.shaixuan),
    path('qu', invv.qu),
    path('deleteInfo',invv.delete),
]
