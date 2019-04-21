import time
import json

'''
    Command list:
    -1 means not command
    1 means help,
    2 means change state
    4 means ask current style
'''

def CommandDoit(str, openid, user):
    #make sure str is one of commands
    if str == 'help':
        NormalHelp = '''Help:
            /(command) means command:
                # Normal Commands
                /help : Get help
                /trans : Change state to Translation
                /talk : Change state to Talking with Tencent AI
                /ocr : Change to ocr recongnition
                /pictrans : Change to picture translation
                /mode : Ask for current mode
                '''
        OpHelp = '''# Op Commands
                /list : Return list of all users
                /list-openid : Return list of all users' openid
                /op (openid): Give op to someone
                /delop (openid): Delete Op of someone
                /ban (openid) : Ban someone
                /unban (openid) : Unban someone
            '''
        ExtraHelp = '''normal string or image:
                The string or image will be sent to Tencent AI to translation, talking ...'''

        if user.list[openid].IsOp:
            res = NormalHelp + OpHelp + ExtraHelp
        else:
            res = NormalHelp + ExtraHelp
        return res

    #2 means change state while 1 means translation, see Action list in Doit.py
    if str == 'trans':
        user.list[openid].MsgStyle = 1
        return 'Successful'
    elif str == 'talk':
        user.list[openid].MsgStyle = 2
        return 'Successful'
    elif str == 'ocr':
        user.list[openid].ImgStyle = 1
        return 'Successful'
    elif str == 'pictrans':
        user.list[openid].ImgStyle = 2
        return 'Successful'

    elif str == 'mode':
        # TODO:
        MsgCode = user.list[openid].MsgStyle
        ImgCode = user.list[openid].ImgStyle

        MsgStyleList = ('None', 'Translation', 'Talk')
        ImgStyleList = ('None', 'Ocr Recongnition', 'Picture Translation')
        return 'Current message style is {0}.\nCurrent image style is {1}.'.format(MsgStyleList[MsgCode], ImgStyleList[ImgCode])

    elif user.list[openid].IsOp:
        # They are Op Command
        str = str.split(' ')
        if str[0] == 'list':
            res = user.GetList()
            res = json.dumps(res)
            return res
        if str[0] == 'list-openid':
            res = [man.openid for man in user.list.values()]
            res = json.dumps(res)
            return res

        if len(str) == 2:
            if str[0] == 'op':
                res = user.GiveOpToUser(str[1])
            if str[0] == 'delop':
                res = user.DeleteOpOfUser(str[1])
            if str[0] == 'ban':
                res = user.BanSomeone(str[1])
            if str[0] == 'unban':
                res = user.UnBanSomeone(str[1])
            return res
        else:
            return 'Command Format Wrong.'

    else:
        return "No such Command."



def IsCommand(str):
    if str[0] == '/':
        return True
    else:
        return False

