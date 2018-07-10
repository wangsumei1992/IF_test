from datetime import datetime
import hashlib, binascii, os, sys, requests
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/data_configuration/")
from get_data import GetData
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
def get_stampToken():
    return int(datetime.now().timestamp()*1000)

# def get_chekToken_old(*args):
# #     md5 = hashlib.md5()
# #     str_code = ""
# #     for i in args:
# #         str_code = str_code + i
# #    # a = list(args)
# #     #a.sort()
# #     md5.update(str_code.encode('utf-8'))
# #     return md5.hexdigest()

def get_chekToken(**kwargs):
    md5 = hashlib.md5()
    str_code = ""
    values = list(dict(sorted(kwargs.items(),key=lambda d :d[0])).values())
    for i in values:
        str_code = str_code + i
    md5.update((str_code+"689d3783957d65d57229ba3dc70a20fb").encode('utf-8'))
    return md5.hexdigest()


# 登录密码加密
def get_loginpass(accesskey, loginpass):
    PADDING = '\0'
    BS = 16
    pad1 = lambda s: s + (BS - len(s) % BS) * PADDING
    obj = AES.new(str.encode(accesskey), AES.MODE_CBC, str.encode('a03a7f034e134f50'))
    message = pad1(loginpass)
    ciphertext = obj.encrypt(str.encode(message))
    # return binascii.b2a_hex(ciphertext)
    # print(ciphertext)
    return binascii.hexlify(ciphertext)



# 解密函数
def decrpy_wq(accesskey, data):
    # data = get_loginpass("a03a7f034e134f50", "00000")
    PADDING = '\0'
    BS = 16
    obj = AES.new(str.encode(accesskey), AES.MODE_CBC, str.encode('a03a7f034e134f50'))
    decr = obj.decrypt(binascii.unhexlify(data))
    return (decr.decode().strip('\0'))


# 获取authtoken
def get_auth_token(userName='15458524695', loginPass='15458524695', checkToken="111", sessionKey="123"):
    sessionkey_url = GetData.url + "/createValidateCode"
    accessKey_url = GetData.url + "/token/accessToken"
    url_login = GetData.url + "/user/login"

    # 获取图形验证码
    requests.request('post', url=sessionkey_url, data={'sessionKey': sessionKey})
    # 获取accessKey
    response = requests.request('post', url=accessKey_url, data={'userName': userName})
    #print(response)
    accessKey = response.json()['data']
    loginpass_encrypt = get_loginpass(accessKey, loginPass)
    data = {'checkToken': checkToken, 'device_id': "222", 'loginPass': loginpass_encrypt,
            'sessionKey': sessionKey, 'source': "WEB", 'userName': userName, 'validateCode': "1"}
    r = requests.request('post', url=url_login, data=data)
    result = r.json()
    #print(result)
    auth_token = result['data']['authToken']
    return auth_token


class Crypt(object):
    secret_key = 'a03a7f034e134f50'
    iv = 'a03a7f034e134f50'

    def encypt(self, s):
        # 加密
        PADDING = '\0'
        pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
        msg = pad(str.encode(s), 16, style='iso7816')
        print('输出byte string类型：')
        print(str.encode(self.iv))
        cipher = AES.new(str.encode(self.secret_key), AES.MODE_CBC, str.encode(self.iv))
        # cipher = AES.new(self.secret_key, AES.MODE_CBC, self.iv)
        # print('b')
        # print(msg)
        print(pad_it(s))
        d = pad_it(s)
        # msg = cipher.encrypt(str.encode(d))
        msg = cipher.encrypt(d)
        print('c')
        print("输出加密后的类型：")
        print(type(msg))
        print(binascii.b2a_hex(msg))

        # BS=16
        # pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        # print(len(pad("wq")))
        # print(pad("wq").encode('utf-8'))
        # #print(get_chekToken("wq","sa"))
        #
        # a = {"b":"12", "a":"89","hj":"67"}
        # def sortedDictValues1(adict):
        #     keys = list(adict.keys())
        #     keys.sort()
        #     return [adict[key]  for key  in keys]
        # #print(sortedDictValues1(a))
        #
        # b = sorted(a.items(),key=lambda d :d[1])
        # print(a.items())
        # print(dict(b).values())

            # BS=16
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# print(len(pad("wq")))
# print(pad("wq").encode('utf-8'))
# #print(get_chekToken("wq","sa"))
#
# a = {"b":"12", "a":"89","hj":"67"}
# def sortedDictValues1(adict):
#     keys = list(adict.keys())
#     keys.sort()
#     return [adict[key]  for key  in keys]
# #print(sortedDictValues1(a))
#
# b = sorted(a.items(),key=lambda d :d[1])
# print(a.items())
# print(dict(b).values())


#获取手机验证码-不需要登录
def SmsCode(sessionKey="123", mobilephone="12345678911", smsType="Register"):
    sessionkey_url = GetData.url + "/createValidateCode"
    requests.request('post', url=sessionkey_url, data={'sessionKey': sessionKey})
    url = GetData.url + "/sendMobileCode"
    test_data = {'validateCode': '1', 'sessionKey': sessionKey, 'mobile': mobilephone, 'smsType': smsType}
    r = requests.request('get', url=url, params=test_data)
    result = r.json()
    #print(result)
    #result = r.json()
    #print(result)


# 获取手机验证码-需要登录

def SmsCode_authToken(userName='14458526695', loginPass='14458526695', smsType='ForgotPayPassword',mobile='14458526695'):
    auth_token_sms = get_auth_token(userName, loginPass)
    url = GetData.url + "/sendUserMobileCode"
    test_data = {'authToken': auth_token_sms, 'smsType': smsType, 'mobile': mobile}
    r = requests.request('post', url=url, data=test_data)
    result = r.json()
   # print(result)

    #result = r.json()
    #print(result)
