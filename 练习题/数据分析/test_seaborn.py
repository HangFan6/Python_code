# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月13日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # SimHei表示黑体
plt.rcParams['axes.unicode_minus'] = False  # 运行配置参数总的轴（axes）正常显示正负号（minus）

'''基础操作'''
# example=pd.DataFrame(np.random.random(200).reshape(50,4),columns=['x1','y1','a1','b1'])
# # print(example)
# plt.figure(1)
# sns.scatterplot(x=example['x1'],y=example['y1'])
# plt.figure(2)
# sns.scatterplot(data=example)  # x轴为序号值
# plt.figure(3)
# sns.set(style='dark')  # 默认设置背景色darkgrid（带网格暗色）
# # (全局样式设置) style: white、dark、whitegrid、darkgrid
# sns.scatterplot(data=example,x='x1',y='y1')  # 指定x轴与对应的y值
# plt.figure(4)
# sns.scatterplot(data=example,x='a1',y='b1')  # 指定x轴与对应的y值
# plt.show()

'''导入数据集'''
"""国外网站，联网获取数据较慢，建议使用本地数获取"""
# # 获取数据集列表
names=sns.get_dataset_names()
print(names)  # 查看数据集的名字
# 下载数据集
data=sns.load_dataset('titanic',data_home=r'C:\Users\26915\seaborn-data',cache=True)  # cache=True 表示从本地加载数据
print(data)
print(data.columns)
# hue：数据类型拆分（通过颜色区分）  style：数据类型拆分（通过标记符号区分）
sns.scatterplot(data=data,x='fare',y='age',hue='survived',style='sex')
plt.show()






