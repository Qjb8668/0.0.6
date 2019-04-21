import urllib.request
import requests
import base64
import GetParamsInTxai as getpm

def Ocr(ImageUrl):
    file = urllib.request.urlopen(ImageUrl)
    image = base64.b64encode(file.read())
    ParamsExtra = {
        'image' : image
    }
    Params = getpm.GetParams(ParamsExtra)
    url = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'
    try:
        res = requests.post(url, Params).json()
        if res == None:
            print('kongkong')
            return 'kongkong'
        print('****')
        if res['ret'] == 0:
            data = res['data']
            item_list = data['item_list']
            res = ''
            for item in item_list:
                res += (item['itemstring'] + '\n')
            return res
        else:
            ret = res['ret']
            msg = res['msg']
            res = 'Ocr wrong:{0} {1}.'.format(ret, msg)
            print(res)
            return res
    except Exception as e:
        res = 'Ocr Wrong:' + str(e)
        print(res)
        return res

