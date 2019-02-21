from django.http import JsonResponse
from django.shortcuts import render

from lib.sms import send_vcode


def submit_vcode(request):
    # 前段获取手机号
    phone = request.GET.get('phone')
    print(phone)
    send_vcode(phone)
    print("b")
    return JsonResponse({'msg': 'ok'})