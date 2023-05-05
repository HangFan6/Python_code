# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月05日
"""
import numpy as np
import pandas as pd

data = {'语文': [95, 50, 100, 90, 86, 94, 73, 30],
 '数学': [86, 81, 77, 98, 86, 55, 47, 60],
 '英语': [93, 96, 82, 73, 59, 68, 71, 50]}
labels = ['小慕', '小明', '小兰', '张三', '小花', '小田', '王五', '小丽']
excel=pd.DataFrame(data,index=labels)
print(excel)
print(excel[excel>60].dropna())
print(np.average(excel['语文']),np.average(excel['数学']),np.average(excel['英语']))
total=excel.sum(axis=1)
print(total)
print(total.sort_values(ascending=False))


