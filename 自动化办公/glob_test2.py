# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月08日
"""
# =========查找含有指定内容的文件==================
import glob   # glob中包含os模块
final_result = []
def search(path,target):
    result = glob.glob(path)

    for data in result:
        if glob.os.path.isdir(data):
            _path=glob.os.path.join(data,'*')
            search(_path,target)
        else:
            # 源文件打开时是gbk编码格式，无法读取；若要读取，需设定文件打开时为utf-8编码格式
            f=open(data,'r',encoding='utf-8')
            # 对于一些文件是不可读文件，如压缩文件
            try:
                content=f.read()
                if target in content:
                    final_result.append(data)
            except:
                print('data read failed: %s'% data)
                f.close()
                continue
            finally:
                f.close()
    return final_result

if __name__=='__main__':
    path = glob.os.path.join(glob.os.getcwd(), '*')
    result=search(path,target='dewei')
    print(result)



