#-*- coding:utf-8 -*-
from django.contrib import admin
from weixin.models import AppToken, MyUser

# Register your models here.
admin.site.register(AppToken)
admin.site.register(MyUser)