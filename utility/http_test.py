# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib

url = "https://www.baidu.com"
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}

cookiejar = cookielib.CookieJar()

request = urllib2.Request(url, headers = headers)
request.add_header('Content-Length', '0')


httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
cookieProcessor = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(httpHandler, httpsHandler, cookieProcessor)

#urllib2.install_opener(opener)
#response = urllib2.urlopen(request)

response = opener.open(request)

print '*********response url*************'
print response.geturl()
print '*********response info************'
print response.info()
print response.read()