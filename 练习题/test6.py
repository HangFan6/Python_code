# -*- coding:utf-8 -*-
"""
作者：HET
clock装饰器
日期：2023年03月30日
"""
import time
# clock装饰器
def clock(func):
    def clocked(*args, **kwargs):
        # 起始时间
        start=time.time()
        # 程序执行
        ret=func(*args, **kwargs)
        # 结束时间
        end=time.time()
        # 输出
        print(func.__name__, end - start)
        return ret
    return clocked

@clock
def test():
    print('装饰器……')
    time.sleep(5)
test()