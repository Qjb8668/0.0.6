import requests
import base64
import urllib.request
import GetParamsInTxai as getpm

def PictureTranslation(ImagerUrl, id, scene = 'doc', source = 'auto', target = 'auto'):
    file = urllib.request.urlopen(ImagerUrl)
    image = base64.b64encode(file.read())
    ParamsExtra = {
        'image' : image,
        'session_id' : id,
        'scene' : scene,
        'source' : source,
        'target' : target
    }
    Params = getpm.GetParams(ParamsExtra)
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_imagetranslate'
    res = requests.post(url, Params).json()
    if res['ret'] == 0:
        data = res['data']
        res = ''
        for target in data['image_records']:
            res += target['target_text'] + '\n'
        return res
    else:
        ret = res['ret']
        msg = res['msg']
        res = 'PictureTranslation Wrong:{0} {1}.'.format(ret, msg)
        print(res)
        return res