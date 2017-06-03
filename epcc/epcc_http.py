#-*- coding:utf-8 -*-
import os
import urllib2
import certifi
import requests
from firstsite.settings import BASE_DIR
from requests.utils import DEFAULT_CA_BUNDLE_PATH
cert = os.path.join(BASE_DIR, 'epcc/cert/server.crt' )

encoding = 'utf-8'
class EpccHttpClient(object):
    @staticmethod
    def send_epcc_http(url, data, headers):
        try:
            req = requests.post(url, data.encode(encoding), headers = headers, verify = False)
            result = req.text
            return result
        except Exception, e:
            raise
        
    @staticmethod
    def gen_http_header(ori_issr_id, msg_tp, reserved_field):
        headers = {}
        headers['Content-Type'] = 'application/xml;charset=utf-8'
        headers['MsgTp'] = msg_tp
        headers['OriIssrId'] = ori_issr_id
        headers['ReservedField'] = reserved_field
        return headers
    
if __name__ == '__main__':
    ori_issr_id = 'Z2004944000010'
    msg_tp = 'epcc.101.001.01'
    reserved_field = '1'
    headers = EpccHttpClient.gen_http_header(ori_issr_id, msg_tp, reserved_field)
    data = u'''<?xml version="1.0" encoding="UTF-8"?><root xmlns="namespace_string"><MsgHeader><SndDt>2017-06-20T10:27:42</SndDt><MsgTp>epcc.101.001.01</MsgTp><IssrId>G4000311000018</IssrId><Drctn>22</Drctn><SignSN>4000094892</SignSN><NcrptnSN>4000094892</NcrptnSN><DgtlEnvlp>MIGMAiBIbSYYxhA9ztvIWce/f9s51jMnczFoL2lVLguZ9EmPogIhANbnswxytKwElE/St96W8gfHc65jqV6DSERtWSzHRWYSBCBJ9w5tVGMuhbUCrFkbnhE1wbkvieT3VNPBasFmWcqUBQQjFPF/1i7wHZKvBGWluHDUbzbb+IgaVDy4SgV0YyMyKz40SfI=</DgtlEnvlp></MsgHeader><MsgBody><SgnInf><SgnAcctIssrId>C1010211000012</SgnAcctIssrId><SgnAcctTp>00</SgnAcctTp><SgnAcctId>ou/PlP08jRH97/ZaK0WoEZnnUGz12o6Wye6XvvHy7Ow=</SgnAcctId><SgnAcctNm>4EeQPde8/KFfEus386QqRQ==</SgnAcctNm><IDTp>01</IDTp><IDNo>fFgiW6JXUOgoeZVL1iQs8M0AY8+TbrFhuRrHE3XekMo=</IDNo><MobNo>5U8yI6d1QjYxPFcWcXov1Q==</MobNo></SgnInf><TrxInf><TrxCtgy>0202</TrxCtgy><TrxId>2017062040147000000001441008174</TrxId><TrxDtTm>2017-06-20T10:27:42</TrxDtTm><AuthMsg>843209</AuthMsg></TrxInf><InstgInf><InstgId>Z2004944000010</InstgId><InstgAcct /></InstgInf></MsgBody></root> 
{S:MEUCIFF2e945431ODNt4HXcndWmqtMfC4kviVoQOxBcoI4OrAiEAyMYt5lBAvAEsW9n3IT4c7Agl 
De6tguFLc37Ku1GQ7M8=}'''
    http_url = 'https://114.255.225.8:443/icbc/epcc'
    ret_xml = EpccHttpClient.send_epcc_http(http_url, data, headers)
    print ret_xml
    
    print DEFAULT_CA_BUNDLE_PATH