#-*- coding:utf-8 -*-
import json
from datetime import datetime
from weixin.models import AppToken
from utility.http_interface import HttpInterface

WEIXIN_URL = u'https://api.weixin.qq.com/cgi-bin'

class WeixinApi(object):
    def __init__(self, appid, appsecret):
        self.appid = appid
        self.appsecret = appsecret
        self.weixin_url = WEIXIN_URL
        self.access_token = None
        self.expires_in = None
        

    def update_access_token(self):
        url = self.weixin_url + u'/token'
        data = {}
        data['grant_type'] = 'client_credential'
        data['appid'] = self.appid
        data['secret'] = self.appsecret
        try:
            http_interface = HttpInterface()
            ret = http_interface.send_http(url, data)
            ret_json = json.loads(ret)
            self.access_token = ret_json['access_token']
            self.expires_in = ret_json['expires_in']
        except:
            raise
        
    @property
    def get_access_token(self):
        return self.access_token
    
    def set_access_token(self, access_token):
        self.access_token = access_token
    
    @property
    def get_expires_in(self):
        return self.expires_in
    

    def update_ip_list(self):
        url = self.weixin_url + u'/getcallbackip'
        data = {}
        data['access_token'] = self.access_token
        http_interface = HttpInterface()
        ret = http_interface.send_http(url, data)
        ret_json = json.loads(ret)
        return ret_json['ip_list']
    
    @property
    def get_ip_list(self):
        return self.ip_list
    
    def pull_user_openid(self, next_openid = ''):
        url = self.weixin_url + u'/user/get'
        data = {}
        data['access_token'] = self.access_token
        data['next_openid'] = next_openid
        http_interface = HttpInterface()
        ret = http_interface.send_http(url, data)
        return json.loads(ret)
        
    def get_user_info(self, openid):
        url = self.weixin_url + u'/user/info'
        data = {}
        data['access_token'] = self.access_token
        data['openid'] = openid
        data['lang'] = 'zh_CN'
        http_interface = HttpInterface()
        ret = http_interface.send_http(url, data)
        return json.loads(ret)
        
if __name__ == '__main__':
    weixin_api = WeixinApi('wx8f03130da7bf76f3', '23179288a8d3a752ebd044abe258423e')
    weixin_api.update_access_token()
    print 'access_token:' + weixin_api.get_access_token
    print 'expires_in:%d' % weixin_api.expires_in

    
        