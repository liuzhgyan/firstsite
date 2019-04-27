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
        
    
class CarMaintainDtl(models.Model):
    JOB_CHOICES = (
        (u'1', u'工费'),
        (u'2', u'零件')
        )
    job_name = models.CharField(max_length = 200, null = False, blank = False, verbose_name = u'作业项目')
    job_type = models.CharField(max_length = 2, choices = JOB_CHOICES, null = True, blank = True, verbose_name = u'操作类型')
    count = models.IntegerField(verbose_name = u'数量')
    amount = models.IntegerField(verbose_name = u'费用')
    mileage = models.IntegerField(verbose_name = u'里程')
    work_date = models.DateField(null = False, blank = False, verbose_name = u'保养日期')
    remark = models.CharField(max_length = 200, null = True, blank = True, verbose_name = u'备注')
    
    class Meta:
        verbose_name = u'汽车保养明细'
        ordering = ['-mileage', 'job_type', 'job_name']
    