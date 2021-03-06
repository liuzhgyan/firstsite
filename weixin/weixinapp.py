#-*- coding:utf-8 -*-
import time
from datetime import datetime, timedelta
from weixin.weixinapi import WeixinApi
from weixin.models import AppToken, MyUser


EXPIRES_THRESHOLD = 600
QR_SCENE = 'QR_SCENE'
QR_LIMIT_SCENE = 'QR_LIMIT_SCENE'
QR_LIMIT_STR_SCENE = 'QR_LIMIT_STR_SCENE'
class WeixinApp(object):
    '''
    classdocs
    '''
    def __init__(self, appid):
        '''
        Constructor
        '''
        self.appid = appid
        apptoken = AppToken.objects.get(appid = appid)
        self.appsecret = apptoken.appsecret
        self.access_token = apptoken.access_token
        self.last_access_token = apptoken.last_access_token
        self.update_time = apptoken.update_time
        self.expires_in = apptoken.expires_in
        self.weixin_api = WeixinApi(self.appid, self.appsecret)
        if self.access_token is None or self.update_time is None or self.expires_in is None or (
            self.update_time + timedelta(0, self.expires_in - EXPIRES_THRESHOLD) < datetime.now() ):
            print 'update access token'            
            try:
                self.weixin_api.update_access_token()
                self.last_access_token = self.access_token
                self.access_token = self.weixin_api.get_access_token
                self.expires_in = self.weixin_api.get_expires_in
                self.update_time = datetime.now()
                apptoken.access_token = self.access_token
                apptoken.last_access_token = self.last_access_token
                apptoken.update_time = self.update_time
                apptoken.expires_in = self.expires_in
                apptoken.save()
            except:
                raise
        else:
            print 'access token already updated'
            self.weixin_api.set_access_token(self.access_token)
            
    def pull_user_all(self):
        user_json = self.weixin_api.pull_user_openid()
#         print user_json
        count = user_json['count']
        total = user_json['total']
        data = user_json['data']
        openid_list = data['openid']
        next_openid = user_json['next_openid']
#         for openid in openid_list:
#             print openid
        return openid_list
            
    def pull_user_info(self, openid):
        info = self.weixin_api.get_user_info(openid)
#         for k,v in info.items():
#             print k, v
        return info
    
    def update_user_info(self, openid):
        info = self.pull_user_info(openid)
        tmp_subscribe_time = info['subscribe_time']
        # tmp_subscribe_time 时间戳格式
#         print tmp_subscribe_time
        subscribe_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tmp_subscribe_time))
        try:
            myuser = MyUser.objects.get(openid = openid)
            myuser.nickname = info['nickname']
            myuser.subscribe = info['subscribe']
            myuser.sex = info['sex']
            myuser.city = info['city']
            myuser.country = info['country']
            myuser.province = info['province']
            myuser.language = info['language']
            myuser.headimgurl = info['headimgurl']
            myuser.subscribe_time = subscribe_time
            myuser.remark = info['remark']
            myuser.groupid = info['groupid']
            if info.has_key('unionid'):
                myuser.unionid = info['unionid']
            myuser.update_time = datetime.now()
            myuser.save()
        except MyUser.DoesNotExist:
            myuser = MyUser.objects.create(
                openid = openid,
                nickname = info['nickname'],
                subscribe = info['subscribe'],
                sex = info['sex'],
                city = info['city'],
                country = info['country'],
                province = info['province'],
                language = info['language'],
                headimgurl = info['headimgurl'],
                subscribe_time = subscribe_time,
                remark = info['remark'],
                groupid = info['groupid'],
                update_time = datetime.now()
                )
            if info.has_key('unionid'):
                myuser.unionid = info['unionid']
            myuser.save()
            
        

    def create_qrcode(self, scene_id, expire_seconds = 1800, action_name = QR_SCENE):
        ret = self.weixin_api.create_qrcode(scene_id, expire_seconds, action_name)
        return ret['ticket']
    
    def show_qrcode(self, ticket):
        return self.weixin_api.show_qrcode(ticket)
            
if __name__ == '__main__':
    weixin_app = WeixinApp('wx8f03130da7bf76f3')
    user_list = weixin_app.pull_user_all()
    print user_list
    for openid in user_list:
        weixin_app.update_user_info(openid)    
#     ticket = weixin_app.create_qrcode(123, action_name = 'QR_LIMIT_SCENE')
#     print ticket

#     print weixin_app.show_qrcode(ticket)
    
    
    