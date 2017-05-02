#-*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, render_to_response
from weixin.forms import TestDateForm
# Create your views here.

def home(request):
    print request.GET
    if request.GET.has_key('testdate'):
        form = TestDateForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            testdatetime = cd['testdatetime']
            testdate = cd['testdate']
            testtime = cd['testtime']
            print type(testdatetime)
            print type(testdate)
            print type(testtime)
            print testdatetime, testdate, testtime
    else:
        form = TestDateForm()
    return render_to_response('home.html', locals())