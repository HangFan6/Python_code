# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月08日
"""
# =======清理重复的文件=========
import glob
import hashlib

def clear(path):
    result=glob.glob(path)
    for _data in result:
        if glob.os.path.isdir(_data):
            _path=glob.os.path.join(_data,'*')
            clear(_path)
        else:
            name=glob.os.path.split(_data)[-1]
            is_byte=False
            # 读取zip文件
            if 'zip' in name:
                is_byte=True
                f=open(_data,'rb')
            else:
                # 文件中含中文，需设置编码格式
                f=open(_data,'r',encoding='utf-8')
            try:
                content=f.read()
                f.close()
                if is_byte:
                    hash_content_obj=hashlib.md5(content)
                else:
                    hash_content_obj = hashlib.md5(content.encode('utf-8'))
                # 将字符串转成16进制，避免比较内容太多，占用内存
                hash_content=hash_content_obj.hexdigest()
                if name in data:
                    sub_data=data[name]
                    is_delete=False
                    for k,v in sub_data.items():
                        if v==hash_content:
                            glob.os.remove(_data)
                            print('%s will delete'%_data)
                            is_delete=True
                    if not is_delete:
                        data[name][_data]=hash_content
                else:
                    data[name]={_data:hash_content}
            except Exception as e:
                print('error is %s'% e)
                print('data read failed: %s'% _data)
                f.close()
                continue
            finally:
                f.close()

if __name__=='__main__':
    # 不同文件夹下可能有相同文件名，但内容不相同
    # data={'name':{'path1/name':'content','path2/name':'content','...':'...'}}
    data={}
    path=glob.os.path.join(glob.os.getcwd(),'*')
    clear(path)
    for key,value in data.items():
        for _k,_v in value.items():
            print(_k,_v)