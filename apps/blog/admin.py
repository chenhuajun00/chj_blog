#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Article, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # 给content字段添加富文本


admin.site.unregister(Article)  # 先注销，再重新注册
admin.site.register(Article, PostAdmin)
