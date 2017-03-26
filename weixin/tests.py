#-*- coding:utf-8 -*-
import time
from datetime import datetime, timedelta
from django.test import TestCase


# Create your tests here.

subscribe_time = 1490458528
lt = time.localtime(subscribe_time)
print lt
print type(lt)
print time.strftime('%Y-%m-%d %H:%M:%S', lt)
