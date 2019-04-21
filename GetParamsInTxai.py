import time
import random
import GetAuthenticationInTxai as auth

def GetRandomStr():
    AlphaFactory = "abcdefghijklmnopqrstuvwxyz"
    str = ""
    for i in range(15):
        index = random.randint(0, 25)
        str += AlphaFactory[index]
    return str

def GetParams(ParamsExtra):
    params = {
        'app_id' : '2115506023',
        'time_stamp' : int(time.time()),
        'nonce_str' : GetRandomStr(),
    }
    params.update(ParamsExtra)
    params['sign'] = auth.GetSign(params, 'wNtPPdoPqRDHMvQw')
    return params