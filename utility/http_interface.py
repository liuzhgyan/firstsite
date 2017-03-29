# -*- coding: utf-8 -*-
import traceback
from datetime import datetime
from xml.etree import ElementTree as ET
import urllib, urllib2
from utility import myurlencode


class HttpInterface(object):
    
    def send_http(self, url, context = {}, method = 'POST', encoding = 'UTF-8'):
        try:
            req = urllib2.Request(url)
            data = urllib.urlencode(context)
            print data
            #enable cookie
            if method == 'POST':
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
                response = opener.open(req, data, timeout = 5)
                ret = response.read()
            elif method == 'GET':
                geturl = u'%s?%s' % (url, data)
                response = urllib2.urlopen(geturl, timeout = 5)
                ret = response.read()
            else:
                raise '[ERROR]Bad method：%s' % method
            
            result = ret.decode(encoding)
            return urllib.unquote(result)
        except UnicodeDecodeError, e:
            print '[ERROR]UnicodeDecodeError: ret:' + ret
            return urllib.unquote(ret)
        except urllib2.URLError, e:
            print e, traceback.format_exc()
            return None
        except Exception, e:
            print e, traceback.format_exc()
            raise
        
    def send_https(self, url, context, method = 'POST', encoding = 'UTF-8'):
        try:
            req = urllib2.Request(url)
#             data = urllib.urlencode(context)
#             print context
            data = context.replace("'", '"')
#             print urllib.unquote(data)
            #enable cookie
            if method == 'POST':
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(), urllib2.HTTPSHandler(debuglevel=0))
                response = opener.open(req, data, timeout = 5)
                ret = response.read()
            elif method == 'GET':
                geturl = u'%s?%s' % (url, data)
                response = urllib2.urlopen(geturl, timeout = 5)
                ret = response.read()
            else:
                raise '[ERROR]Bad method：%s' % method
            
            result = ret.decode(encoding)
            return urllib.unquote(result)
        except UnicodeDecodeError, e:
            print '[ERROR]UnicodeDecodeError: ret:' + ret
            return urllib.unquote(ret)
        except urllib2.URLError, e:
            print e, traceback.format_exc()
            return None
        except Exception, e:
            print e, traceback.format_exc()
            raise
        
    def get_elem_text(self, elem, name):
        result = elem.find(name)
        if result is not None:
            return result.text
        else:
            return None


def test():
    url = u'https://api.weixin.qq.com/cgi-bin/token'
    data = {}
    data['grant_type'] = 'client_credential'
    data['appid'] = 'wx8f03130da7bf76f3'
    data['secret'] = '23179288a8d3a752ebd044abe258423e'
    http_interface = HttpInterface()
    ret = http_interface.send_http(url, data)
    print ret


if __name__ == '__main__':
    test()
    