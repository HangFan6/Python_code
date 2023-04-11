# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月08日
"""
# =========查找指定文件============
import glob   # glob中包含os模块
# 获取当前路径下的所有内容
# 判断每个内容的类型（文件夹还是文件）
# 递归
def search(path,target):
    result = glob.glob(path)
    final_result = []
    for data in result:
        if glob.os.path.isdir(data):
            _path=glob.os.path.join(data,'*')
            # print('%s is filepath' % data)
            search(_path,target)
        else:
            # print('%s is a file' % data)
            if target in data:
                final_result.append(data)
    return final_result

if __name__=='__main__':
    path = glob.os.path.join(glob.os.getcwd(), '*')
    result=search(path,target='test1')
    print(result)


