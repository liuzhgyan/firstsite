#-*- coding:utf-8 -*-
from django.contrib import admin
from account.models import Record
# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('chandate', 'chantype', 'chanflag', 'amt', 'description', 'regdate')
    search_fields = ('chandate', 'chantype', 'chanflag') 
    ordering = ('-chandate',)
    

admin.site.register(Record, RecordAdmin)