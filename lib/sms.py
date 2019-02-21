import random

# 生成验证码
import requests

from swiper.config import YZX_SMS_API, YZX_SMS_PARAMS


def gen_vcode():
    string = ''
    for _ in range(6):
        string += str(random.randint(0, 9))
    return string


# 发送短信
def send_sms(phone, vcode):
    print(vcode)
    params = YZX_SMS_PARAMS.copy()
    params['param'] = vcode
    params['mobile'] = phone
    res = requests.post(YZX_SMS_API, json=params)
    if res.status_code == 200:
        result = res.json()
        print(result)


# 发送验证码
def send_vcode(phone):
    vcode = gen_vcode()
    print(phone)
    send_sms(phone, vcode)