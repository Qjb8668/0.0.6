import requests
import GetParamsInTxai as getpm

def talking(message, id):
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    ParamsExtra = {
        'session' : id,
        'question' : message
    }
    params = getpm.GetParams(ParamsExtra)
    res = requests.get(url, params).json()
    if res['ret'] == 0 :
        data = res['data']
        return data['answer']
    else :
        ret = res['ret']
        msg = res['msg']
        res = 'Talking wrong:{0} {1}.'.format(ret, msg)
        print(res)
        return res
