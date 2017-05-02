#-*- coding:utf-8 -*-
from django import forms

class TestDateForm(forms.Form):
    testdatetime = forms.DateTimeField(required = True, label = u'datetime')
    testdate = forms.DateField(required = True, label = u'date')
    testtime = forms.TimeField(required = True, label = u'time')
