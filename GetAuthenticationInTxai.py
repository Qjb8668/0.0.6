import hashlib
import random
from urllib.parse import urlencode

def GetSign(params, app_key):
    SortDict = sorted(params.items(), key = lambda item: item[0], reverse=False)
    SortDict.append(('app_key', app_key))
    rawtext = urlencode(SortDict).encode()
    sha = hashlib.md5()
    sha.update(rawtext)
    md5text = sha.hexdigest().upper()
    print(md5text)
    return md5text