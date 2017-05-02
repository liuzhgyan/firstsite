#-*- coding:utf-8 -*-
from django.test import TestCase
from utility.pyDes import triple_des, des
import binascii
# Create your tests here.

'''
Test GenMAC:
paramString:0123456789012345
KEKey:9LJN5m3tR4OYrsxw
arrayOfByte:200387876B4C656B
MAC:7990F22E
'''
if __name__ == '__main__':
    param_str = '0123456789012345'
    ke_key = '9LJN5m3tR4OYrsxw'
    param_str_buf = binascii.a2b_hex(param_str)
#     print param_str_buf
    k = triple_des(ke_key)
    d_buf = k.decrypt(param_str_buf)
    d = binascii.b2a_hex(d_buf)
    print 'key hex:' + d
    
    orig_hex = '32323030317C427C'
    orig_buf = binascii.a2b_hex(orig_hex)
    print 'orig_buf:' + orig_buf
    print 'orig_hex:' + orig_hex
    
    
    
    