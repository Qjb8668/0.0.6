import werobot
import urllib.parse
import urllib.request
import json
import requests

def GetAccessToken():
    params = {
        'grant_type' : 'client_credential',
        'app_id' : 'wx11123322da3cb608',
        'secret' : 'b5a0d640a6ae562120b03674b2785ff3'
     }
    url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s" %(params['grant_type'], params['app_id'], params['secret']))
    #params = urllib.parse.urlencode(params)
    res = urllib.request.urlopen(url).read()
    print(res)
    return res['access_token']
