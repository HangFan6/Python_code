# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月13日
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'font.sans-serif': 'SimHei',   # SimHei表示黑体
      'axes.unicode_minus': False}   # 运行配置参数总的轴（axes）正常显示正负号（minus）
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

'''test1 观察一下五首歌曲的每日播放量变化情况'''
# example=pd.read_csv('spotify.csv',index_col='Date')
# example.index=pd.to_datetime(example.index)
# # print(example)
# bymonth=example.resample('M').first()
# print(bymonth)
# sns.set(rc=rc) # 使图表显示中文字体
# sns.lineplot(data=example)
# plt.xlim(pd.to_datetime("2017-04-01"), pd.to_datetime("2018-01-31"))
# plt.tight_layout()
# plt.title('5首流行歌曲的每日播放量（2017-2018）')
# plt.show()
# print(plt.rcParams['font.sans-serif'])

'''test2 什么样的人群保险费用应该高一些？'''
data=pd.read_csv('healthy_data.csv')
# print(data)
sns.set()
plt.figure(1)
sns.scatterplot(data=data,x='bmi',y='charges',hue='smoker')
plt.figure(2)
sns.lmplot(data=data,x='bmi',y='charges',hue='smoker')
plt.show()
sns.swarmplot(data=data,x='smoker',y='charges')
plt.show()




