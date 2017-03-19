#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Record(models.Model):
    chandate = models.CharField(max_length = 8, null = False, blank = False, verbose_name = u'日期')
    chantype = models.CharField(max_length = 10, null = False, blank = False, verbose_name = u'类型')
    chanflag = models.CharField(max_length = 1, null = False, blank = False, verbose_name = u'收支标志')
    amt = models.IntegerField(null = False, blank = False, verbose_name = u'金额')
    description = models.CharField(max_length = 500, null = True, blank = True, verbose_name = u'描述')
    regdate = models.DateTimeField(null = True, blank = True, verbose_name = u'登记时间')
    
    class Meta:
        verbose_name = u'收支记录'
        ordering = ['-chandate']
        
    
    
    