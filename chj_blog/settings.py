#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

"""
Django settings for chj_blog project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#7*)47n1$5-v)@a&@bvnv$s=8_d9vl5x^@22w#a7n!r30(77ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',  # 注册jet.dashboard
    'jet',  # 注册jet，注意：必须加在django.contrib.admin前面
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.blog',  # 注册app
    'django_summernote',  # 注册富文本输入框
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chj_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chj_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 连接MySQL数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chj_blog',  # 数据库名，需要自己新建
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'chj5055110',  # 数据库密码
        'HOST': '127.0.0.1',  # 数据库所在主机名
        'PORT': '3306',  # 数据库端口号
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'  # 语言

TIME_ZONE = 'Asia/Shanghai'  # 时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 配置静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 添加附件（图片、视频、文件等）的存放路径
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


PAGE_NUM = 10  # 每页显示10篇文章

# 后台主题切换
JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default',
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green',
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green',
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet',
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue',
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray',
    },
]

# 富文本编辑器设置及其优化
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    'styleWithSpan': False,

    # Change editor size
    'width': '80%',
    'height': '480',

    # Use proper language setting automatically (default)
    'lang': 'zh-CN',
}

# 是否展示所有菜单
JET_SIDE_MENU_COMPACT = True  # 菜单不是很度多是建议展示True

JET_SIDE_MENU_ITEMS = [
    {
        'label': '内容管理', 'app_label': 'blog', 'items':
        [
            {'name': 'article'},
            {'name': 'tag'},
            {'name': 'category'},
        ]},
    {
        'label': '附件管理', 'app_label': 'django_summernote', 'items':
        [
            {'label': '附件列表', 'name': 'attachment'},
        ]},
    {
        'label': '权限管理', 'items':
        [
            {'name': 'auth.user', 'permissions': ['auth.user']},
            {'name': 'auth.group', 'permissions': ['auth.user']},
        ]},
]
