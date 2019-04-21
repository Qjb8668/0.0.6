import requests
import os
import GetParamsInTxai as getpm

def Translate(message):
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttrans'
    ParamsExtra = {
        'type': 0,
        'text': message
    }
    params = getpm.GetParams(ParamsExtra)
    res = requests.get(url, params).json()
    if res['ret'] == 0:
        data = res['data']
        print(data)
        text = data['trans_text']
        if text == '':
            return 'System is busy.'
        else:
            return text
    else:
        ret = res['ret']
        msg = res['msg']
        res = 'Translation Wrong:{0} {1}.'.format(ret, msg)
        print(res)
        return res
