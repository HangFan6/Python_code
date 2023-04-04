# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月01日
"""
# ========hashlib加密=========
import hashlib
import time

base_sign='nuke'
def custom():
    a_timestamp=int(time.time())
    _token='%s%s'%(base_sign,a_timestamp)   # 加密串+生成时间
    # 生成hashlib对象
    hashobj=hashlib.sha1(_token.encode('utf-8'))    # 需要将bit类型解码
    # 生成a的16进制加密串
    a_token=hashobj.hexdigest()
    # print(a_token)
    return a_token,a_timestamp
def b_service_check(token,timestamp):
    _token='%s%s'%(base_sign,timestamp)
    b_token=hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token==b_token:
        return True
    else:
        return False

if __name__=='__main__':
    need_help_token,timestamp=custom()
    result=b_service_check(need_help_token,timestamp)
    if result==True:
        print("a合法，b服务可以进行帮助")
    else:
        print("a不合法，b服务不可以进行帮助")






