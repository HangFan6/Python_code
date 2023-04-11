# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月11日
"""
# =======批量修改文件名============
import glob
import shutil

def update_name(path):
    result=glob.glob(path)
    # 使用index定位索引值，需搭配使用enumerate枚举
    for index,data in enumerate(result):
        # 判断是否是一个文件夹
        if glob.os.path.isdir(data):
            _path=glob.os.path.join(data,'*')
            update_name(_path)
        else:
            path_list=glob.os.path.split(data)
            name=path_list[-1]
            new_name='%s_%s' % (index,name)  # 行号_name
            new_data=glob.os.path.join(path_list[0],new_name)
            shutil.move(data,new_data)

if __name__=='__main__':
    path=glob.os.path.join(glob.os.getcwd(),'test1')    # 当前文件路径的全部文件
    update_name(path)


