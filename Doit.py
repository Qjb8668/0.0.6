from Style import Translation as trans, Talking as talks, Ocr as ocr, PictureTranslation as pictrans

'''
    Message Style list:
    1 means Translation, 
    2 means Talking,
    Image Style list:
    1 means Ocr Recognition,
    2 means Picture Translation
'''

def doit(openid = None, id = None, MsgStyle = 0, ImgStyle = 0, message = ''):
    if MsgStyle != 0:
        if MsgStyle == 1:
           res = trans.Translate(message)
           return res

        if MsgStyle == 2:
            if not openid:
                print("Do Talking Wrong:open id is empty.")
                return
            res = talks.talking(message, id)
            return res

    if ImgStyle != 0:
        if ImgStyle == 1:
            res = ocr.Ocr(message)
            return res
        if ImgStyle == 2:
            res = pictrans.PictureTranslation(message, id, 'doc', 'auto', 'auto')
            return res
    # TODO: