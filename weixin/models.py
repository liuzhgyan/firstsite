#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class AppToken(models.Model):
    appid = models.CharField(max_length = 20, verbose_name = u'appID')
    appsecret = models.CharField(max_length = 100, verbose_name = u'appsecret')
    access_token = models.CharField(max_length = 200, null = True, verbose_name = u'access token')
    last_access_token = models.CharField(max_length = 200, null = True, verbose_name = u'last access token')
    update_time = models.DateTimeField(null = True, verbose_name = u'update time')
    expires_in = models.IntegerField(null = True, verbose_name = u'expires in')

    class Meta:
        verbose_name = u'App Token'
        ordering = ['appid']
        
class MyUser(models.Model):
    openid = models.CharField(max_length = 40, verbose_name = u'openid')
    nickname = models.CharField(max_length = 40, null = True, verbose_name = u'nickname')
    subscribe = models.CharField(max_length = 1, null = True, verbose_name = u'subscribe')
    sex = models.CharField(max_length = 1, null = True, verbose_name = u'sex')
    city = models.CharField(max_length = 20, null = True, verbose_name = u'city')
    country = models.CharField(max_length = 20, null = True, verbose_name = u'country')
    province = models.CharField(max_length = 20, null = True, verbose_name = u'province')
    language = models.CharField(max_length = 10, null = True, verbose_name = u'language')
    headimgurl = models.CharField(max_length = 200, null = True, verbose_name = u'headimgurl')
    subscribe_time = models.CharField(max_length = 20, null = True, verbose_name = u'subscribe_time')
    unionid = models.CharField(max_length = 40, null = True, verbose_name = u'unionid')
    remark = models.CharField(max_length = 20, null = True, verbose_name = u'remark')
    groupid = models.CharField(max_length = 2, null = True, verbose_name = u'groupid')
    update_time = models.DateTimeField(null = True, verbose_name = u'update time')
    
    class Meta:
        verbose_name = u'My User'
        ordering = ['openid']