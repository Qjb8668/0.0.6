import json

class User:
    def __init__(self, openid, id, IsOp = 0, IsBanned = 0, MsgStyle = 1, ImgStyle = 1):
        self.openid = openid
        self.id = id
        self.IsOp = IsOp
        self.IsBanned = IsBanned
        self.MsgStyle = MsgStyle
        self.ImgStyle = ImgStyle

    def ConvertToDictionary(self):
        res = {}
        res['openid'] = self.openid
        res['id'] = self.id
        res['IsOp'] = self.IsOp
        res['IsBanned'] = self.IsBanned
        res['MsgStyle'] = self.MsgStyle
        res['ImgStyle'] = self.ImgStyle
        return res


class UserManage:
    DefaultMessageStyle = 1
    DefaultImageStyle = 1
    IdFactory = [i for i in range(10000, 20000)]

    def __init__(self):
        UserFile = open('./user/user.json', 'rb')
        tmp = UserFile.read().decode(encoding = 'utf-8')
        content = json.loads(tmp)
        # sum means the number of all user
        self.sum = content['sum']
        self.list = {}
        for man in content['data']:
            # TODO :
            tmp = User(man['openid'], man['id'], man['IsOp'], man['IsBanned'], man['MsgStyle'], man['ImgStyle'])
            self.list[man['openid']] = tmp
        UserFile.close()

        OpFile = open('./user/op.json', 'rb')
        tmp = OpFile.read().decode(encoding = 'utf-8')
        content = json.loads(tmp)
        self.opsum = content['sum']
        self.op = content['data']
        for openid in self.op:
            self.list[openid].IsOp = 1
            print('Give Op to {0}.'.format(openid))
        OpFile.close()

    def GetAnId(self):
        return self.IdFactory.pop(0)

    def ReturnAnId(self, id):
        self.IdFactory.append(id)
        self.IdFactory.sort(cmp = None, key = None, reverse = False)

    def AddUser(self, openid):
        tmp_id = self.GetAnId()
        tmp = User(openid, tmp_id, 0, 0, self.DefaultMessageStyle, self.DefaultImageStyle)
        self.list[openid] = tmp
        self.sum += 1

    def DeleteUser(self, openid):
        if openid in self.list.keys():
            self.ReturnAnId(self.list[openid].id)
            del(self.list[openid])
            self.sum -= 1
            if openid in self.op:
                index = self.op.index(openid)
                del(self.op[index])
                self.opsum -= 1
        else:
            print('DeleteUser Wrong:{0} is not in UserList.'.format(openid))

    def GiveOpToUser(self, openid):
        # the openid must be in UserList Now
        if openid in self.list.keys():
            if openid in self.op:
                res = 'GiveOpToUser Wrong:{0} has been in OpList'.format(openid)
                print(res)
                return res
            else:
                self.list[openid].IsOp = 1
                self.op.append(openid)
                self.opsum += 1
                res = 'Give Op to {0}. Done.'.format(str[1])
                print(res)
                return res
        else:
            res = 'GiveOpToUser Wrong:{0} is not in UserList'.format(openid)
            print(res)
            return res

    def DeleteOpOfUser(self,openid):
        # the id must be in UserList and OpList Now
        if openid in self.list.keys():
            if openid in self.op:
                index = self.op.index(openid)
                del(self.op[index])
                self.list[open].IsOp = 0
                self.opsum -= 1
            else:
                res = 'DeleteOpOfUser Wrong:{0} is not in OpList'.format(openid)
                print(res)
                return res
        else:
            res = 'DeleteOpOfUser Wrong:{0} is not in UserList'.format(openid)
            print(res)
            return res

    def CheckAndAddUser(self, openid):
        if openid in self.list.keys():
            print('CheckAndAddUser Wrong:{0} has been in UserList'.format(openid))
            print(openid.encode())
            return 0
        else:
            self.AddUser(openid)
            print('CheckAndAddUser Success:{0} has been added in UserList'.format(openid))
            self.UpdateUserList()
            return 1
        return -1
        # return 0 means openid has been in UserList, 1 means has been added to UseList successfully,
        #        -1 means unknown wrong

    def ChangeMsgStyle(self, openid, style):
        # TODO :
        # Check if openid in list
        self.list[openid].MsgStyle = style

    def ChangeImgStyle(self, openid, style):
        # TODO :
        # Check if openid in list
        self.list[openid].ImgStyle = style

    def BanSomeone(self, openid):
        # TODO:
        # Check if openid in list
        if openid in self.list.keys():
            self.list[openid].IsBanned = 1
            res = 'Ban {0}. Done.'.format(str[1])
            print(res)
            return res
        else:
            res = 'BanSomeone Wrong:{0} is not in UserList'.format(openid)
            print(res)
            return res

    def UnBanSomeone(self, openid):
        # TODO:
        # Check if openid in list
        if openid in self.list.keys():
            self.list[openid].IsBanned = 0
            res = 'UnBan {0}. Done.'.format(str[1])
            print(res)
            return res
        else:
            res = 'UnBanSomeone Wrong:{0} is not in UserList'.format(openid)
            print(res)
            return res

    def GetList(self):
        res = {}
        res['sum'] = self.sum
        res['data'] = []
        #res = [man.ConvertToDictionary() for man in self.list.values()]
        print(self.list)
        for man in self.list.values():
            res['data'].append(man.ConvertToDictionary())
        return res

    def UpdateUserList(self):
        UserFile = open('./user/user.json', 'wb')
        content = self.GetList()
        tmp = json.dumps(content).encode(encoding = 'utf-8')
        UserFile.write(tmp)
        UserFile.close()

        OpFile = open('./user/op.json', 'wb')
        content = {
            'sum' : self.opsum,
            'data' : self.op
        }
        tmp = json.dumps(content).encode(encoding = 'utf-8')
        OpFile.write(tmp)
        OpFile.close()




