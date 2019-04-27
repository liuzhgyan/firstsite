#-*- coding:utf-8 -*-
from django.contrib import admin
from account.models import Record, CarMaintainDtl
# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('chandate', 'chantype', 'chanflag', 'amt', 'description', 'regdate')
    search_fields = ('chandate', 'chantype', 'chanflag') 
    ordering = ('-chandate',)
    
class CarMaintainDtlAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_type', 'count', 'amount', 'mileage', 'work_date', 'remark')
    search_fields = ('job_name', 'job_type','mileage')
    ordering = ('-mileage', 'job_type', 'job_name')
    

admin.site.register(Record, RecordAdmin)
admin.site.register(CarMaintainDtl, CarMaintainDtlAdmin)