#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

"""chj_blog URL Configuration

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
from apps.blog import views

from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 主页
    path('home/', views.home, name='home'),  # 主页
    path('articles/<int:id>/', views.detail, name='detail'),  # 文章详情
    path('category/<int:id>/', views.search_category, name='category_menu'),  # 分类搜索
    path('tag/<str:tag>/', views.search_tag, name='search_tag'),  # 标签搜索
    path('summernote/', include('django_summernote.urls')),  # 富文本输入框
    path('jet/', include('jet.urls', 'jet')),  # jet路径
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # jet.dashboard路径
    path('resume/', views.resume, name='resume'),  # 简历路径
    path('weixin/', views.weixin, name='weixin'),  # 微信路径
    path('download/', views.download, name='download')  # 下载中心
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
