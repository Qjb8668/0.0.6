import werobot
import UserManage
import Command
import time
import Doit

robot=werobot.WeRoBot(token='WechatToken')

#@robot.handler
#def hello(message):
#    return message.content 

@robot.handler
def echo(message):
    openid = message.source
    type = message.type

    # Check if he is bannned
    if user.list[openid].IsBanned:
        return "You are banned!"

    start = time.time()
    user.CheckAndAddUser(openid)
    if type == 'text':
        content = message.content
        IsCmd = Command.IsCommand(content)
        if IsCmd:
            NewContent = content[1:]
            res = Command.CommandDoit(NewContent, openid, user)
        else:
            MsgStyle = user.list[openid].MsgStyle
            res = Doit.doit(openid, user.list[openid].id, MsgStyle, 0, content)

    if type == 'image':
        img = message.img
        ImgStyle = user.list[openid].ImgStyle
        res = Doit.doit(openid, user.list[openid].id, 0, ImgStyle, img)

    if type == 'voice':
        res = message.recognition
        print(res)
        if res == None:
            res = 'Try again'

    end = time.time()
    if (end - start) > 5:
        res = 'Time out.'
        print(res)
    return res

#@robot.image
#def img(message):
#    return message.img

if __name__ == '__main__':
    user = UserManage.UserManage()

    # 让服务器监听在 0.0.0.0:80
    robot.config['HOST']='0.0.0.0'
    robot.config['PORT']=80
    robot.config['APP_ID']='wx11123322da3cb608'
    robot.config['ENCODING_AES_KEY']='N9T6k1kR2jELZr8QJAP0A3FGo3gh3PaHgAr4bKqHYo8'

    robot.run()

