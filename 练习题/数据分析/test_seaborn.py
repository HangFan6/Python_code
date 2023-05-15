# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月13日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


'''plt.show() 每次最多能显示两张图'''

'''基础操作'''
# example=pd.DataFrame(np.random.random(200).reshape(50,4),columns=['x1','y1','a1','b1'])
# # print(example)
# plt.figure(1)
# sns.scatterplot(x=example['x1'],y=example['y1'])
# plt.figure(2)
# sns.scatterplot(data=example)  # x轴为序号值
# plt.figure(3)
# sns.set(style='dark')  # 默认设置背景色darkgrid（带网格暗色）
# # (全局样式设置) style: white、dark、whitegrid、darkgrid、ticks(带刻度线)
# sns.scatterplot(data=example,x='x1',y='y1')  # 指定x轴与对应的y值
# plt.figure(4)
# sns.scatterplot(data=example,x='a1',y='b1')  # 指定x轴与对应的y值
# plt.show()

'''导入数据集'''
"""国外网站，联网获取数据较慢，建议使用本地数获取"""
# # # 获取数据集列表
# names=sns.get_dataset_names()
# print(names)  # 查看数据集的名字
# # 下载数据集
# data=sns.load_dataset('titanic',data_home=r'C:\Users\26915\seaborn-data',cache=True)  # cache=True 表示从本地加载数据
# print(data)
# print(data.columns)
# # hue：数据类型拆分（通过颜色区分）  style：数据类型拆分（通过标记符号区分）
# sns.scatterplot(data=data,x='fare',y='age',hue='survived',style='sex')
# plt.show()

'''关系图 价格走势'''
# # 导入指数数据
# example=pd.read_csv('index_close_price.csv',index_col='date')
# # 000016.XSHG：上证50   000905.XSHG：中证500   000300.XSHG：沪深300   399673.XSHE：创业版50
# # print(example.describe())
# # 部分数据绘制：调整为月收盘价 -> 完整绘制 -> 数据解读（可能的偏差）
# sns.set()
# plt.figure(figsize=(10,7))
# sns.lineplot(data=example[:50])
# plt.xticks(rotation=45)  # x轴标签倾斜45°
# plt.tight_layout()  # 使图表大小与画板大小更加紧密贴合
# # =========调整index为日期型=======
# example.index=pd.to_datetime(example.index)
# # 明确日期型，绘图时可以自动选择合适的周期进行绘制
# # print(example.index)
# plt.figure(figsize=(10,7))
# sns.lineplot(data=example[:50])
# plt.tight_layout()  # 使图表大小与画板大小更加紧密贴合
# plt.show()
# # 调整时间频率：日->月
# bymonth=example.resample('M').first()
# print(bymonth)
# sns.lineplot(data=example)  # 按月度绘制收盘价趋势线
# # ========计算、绘制涨跌幅=========
# # 收益率、涨跌幅=（期末值-期中值）/期初值
# print(bymonth.shift(1))  # 将原数据后移1行，作为期初值
# byrate=(bymonth-bymonth.shift(1))/bymonth.shift(1)
# print(byrate)
# # * 方法2 *
# byrate=bymonth.pct_change()
# sns.relplot(data=byrate,kind='line')  # kind='line'表示折线图
# plt.show()
# # ========统一基点：初始值为1000，收盘价=基点*（1+涨跌幅）=============
# bases=byrate
# bases.iloc[0]=1000
# bases.iloc[1:]=1+bases.iloc[1:]
# bases=bases.cumprod()
# print(bases)
# sns.lineplot(data=bases)
# plt.show()

'''分布图'''
# sample=pd.read_csv('index_close_price.csv',index_col='date')
# sample.index=pd.to_datetime(sample.index)  # 调整index类型
# bymonth=sample.resample('M').first()  # 月收盘价
# byrate=bymonth.pct_change()   # 月涨跌幅
# # 整体表现：日涨跌幅、月涨跌幅
# dayrate=sample.pct_change()
# sns.set()  # 设置样式
# plt.figure(1)
# sns.distplot(dayrate,bins=100)  # 日涨跌幅
# plt.figure(2)
# sns.distplot(byrate,bins=50)  # 月涨跌幅
# plt.show()
# indexs=byrate.columns.tolist()
# for i in indexs:
#     sns.distplot(byrate[i],bins=50)
# plt.xlabel('rate')
# plt.ylabel('count')
# plt.show()

'''类别图'''
# sample=pd.read_csv('index_close_price.csv',index_col='date')
# sample.index=pd.to_datetime(sample.index)  # 调整index类型
# bymonth=sample.resample('M').first()  # 月收盘价
# monthrate=bymonth.pct_change()   # 月涨跌幅
# dayrate=sample.pct_change()  # 日涨跌幅
# cols=sample.columns.tolist()  # 获取列标签
# # 箱型图：日涨跌幅、月涨跌幅
# sns.set()
# plt.figure(1)
# sns.boxplot(data=dayrate)
# sns.swarmplot(data=dayrate)  # 加入数据散点（非重叠）
# plt.ylim(-0.050,0.050)
# plt.figure(2)
# sns.boxplot(data=dayrate)
# sns.stripplot(data=dayrate)  # 加入数据散点（重叠）
# plt.ylim(-0.050,0.050)
# plt.show()
# # 计算、可视化年收益率
# byyear=sample.resample('Y').first()  # 年收盘价
# yearrate=byyear.pct_change()  # 年涨跌幅
# sns.boxplot(data=yearrate)
# sns.stripplot(data=yearrate)  # 加入数据散点（重叠）
# # plt.ylim(-0.050,0.050)
# plt.show()

'''回归图'''
# # 回归示例：账单金额vs消费金额、加入性别/烟民标签、加入日期标签
# tips=sns.load_dataset('tips',data_home=r'C:\Users\26915\seaborn-data',cache=True)  # cache=True 表示从本地加载数据
# # print(tips)
# plt.figure(1)
# sns.lmplot(data=tips,x='total_bill',y='tip')
# plt.figure(2)
# sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex',col='smoker')
# plt.show()

sample=pd.read_csv('index_close_price.csv',index_col='date')
sample.index=pd.to_datetime(sample.index)  # 调整index类型
bymonth=sample.resample('M').first()  # 月收盘价
dayrate=sample.pct_change()  # 日涨跌幅
monthrate=bymonth.pct_change()   # 月涨跌幅
byyear=sample.resample('Y').first()  # 年收盘价
yearrate=byyear.pct_change()  # 年涨跌幅
cols=sample.columns.tolist()  # 获取列标签
# 月涨跌幅
# monthrate['date']=monthrate.index  # ** 日期无法做回归性 **
# sns.lmplot(data=monthrate,x='date',y='000016.XSHG')
monthrate['index']=np.arange(len(monthrate))
# 绘制4中类型 回归图
# 方法1：循环
for c in cols:
    sns.lmplot(data=monthrate,x='index',y=c)
plt.show()
# 方法2：改变数据结构
temp=pd.DataFrame()
res=pd.DataFrame()
for c in cols:
    temp['rate']=monthrate[c]
    temp['tag']=c
    temp['index']=np.arange(len(monthrate))  # 统一x轴
    res=res.append(temp)
# res['index']=np.arange(len(res))  # 使用不同x轴
sns.lmplot(data=res,x='index',y='rate',hue='tag')
plt.show()





