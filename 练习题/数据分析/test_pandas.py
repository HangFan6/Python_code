# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月05日
"""
import numpy as np
import pandas as pd
import pandas_datareader as pdr

# # 创建一张二维表格
# data={'apple':[2,3,5,7],'orange':[5,4,8,9]}
# data=pd.DataFrame(data)
# apple=data['apple']
# print(apple)
# apple=pd.Series(apple,index=[3,2,1,0])  # 排序
# print(apple)
# new=apple.reset_index(drop=True)  # 索引重置
# print(new)


# data=np.arange(15).reshape(3,5)
# excel=pd.DataFrame(data,columns=['a','b','c','d','e'])
# print(excel)
# print(excel.values)


# # 创建dataframe：带时间戳的价格数据
# dates=pd.date_range('20210101',periods=30,freq='M')
# data=pd.DataFrame(np.random.rand(30,3),columns=list('ABC'),index=dates)
# print(data)
# # ======头部数据、尾部数据=======
# print(data.head())  # 头部 默认前5行数据
# print(data.tail())  # 尾部 默认后5行数据
# # ========索引、行/列名=========
# print(data.index)  # 行名
# print(data.columns)  # 列名
# # =========查看数值=============
# print(data.values)
# print(data.to_numpy())  # 二维数组
# # =========查看统计摘要==========
# print(data.describe())  # 计数、均值、方差等

# # ***********查询**************
# # 创建dataframe：带时间戳的价格数据
# dates=pd.date_range('20210101',periods=30,freq='M')
# data=pd.DataFrame(np.random.rand(30,3),columns=list('ABC'),index=dates)
# # =========列数据============
# print(data[['A','B']])
# # =========行数据============
# print(data.iloc[3:6])  # 索引3~6行
# print(data.loc['20210101':'20210607','B':'C'])  # 同时对行、列进行筛选
# # =========按值筛选==========
# data=round(data,2)  # 数值保留2位小数
# print(data[data['A']==0.7])
# # =========按条件筛选（布尔值）======
# print(data[data['A']>=0.6])
# data=data[data>0.3]
# print(data)  # 不满足条件的值为NaN
# print(data.dropna())   # 去缺失值
# # =========转置、排序=============
# print(data.T)
# print(data.sort_values(['A','B'],ascending=False))  # 降序


# 5年10年份美国债券收益数据
# data=pdr.get_data_fred('GS10')  # GS10 是一个数据接口
# print(data)
# x=data.resample(rule='Y').mean()   # 均值
# print(x)
# x=data.resample(rule='Y').std().max()   # 标准差 最大值
# print(x)
# x=data.resample(rule='Y').prod()   # 累乘
# print(x)


# 数据合并
data=pdr.get_data_fred('GS10')
data2=pdr.get_data_fred('GS5')
data['GS5']=data2  # 值和index的精确匹配
data['mean']=(data['GS10']+data['GS5'])/2
print(data)

# 周期转换
x=data.resample(rule='Y').last()  # frist()
print(x)  # 每年最后一月数据



