# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月01日
"""
import base64

"""
解决加密可破解问题:
对加密的base64字符串进行二次输出
"""
replace_one='%'
replace_two='$'

def encode(data):
    if isinstance(data,str):
        data=data.encode('utf-8')
    elif isinstance(data,bytes):
        data=data
    else:
        raise TypeError('data need bytes or str')
    _data= base64.encodebytes(data).decode('utf-8')

    _data=_data.replace('a',replace_one).replace('5',replace_two)  # 进行编码替换
    return _data
def decode(data):
    if not isinstance(data,bytes):
        raise TypeError('data need bytes')

    replace_one_b=replace_one.encode('utf-8')
    replace_two_b=replace_two.encode('utf-8')
    data=data.replace(replace_one_b,b'a').replace(replace_two_b,b'5')   # 进行解码替换
    return base64.decodebytes(data).decode('utf-8')


if __name__=='__main__':
    result=encode('hello 小慕')
    print(result)
    new_result=decode(result.encode('utf-8'))
    print(new_result)