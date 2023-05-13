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
# # (全局样式设置) style: white、dark、whitegrid、darkgrid
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
# 导入指数数据
example=pd.read_csv('index_close_price.csv',index_col='date')
# 000016.XSHG：上证50   000905.XSHG：中证500   000300.XSHG：沪深300   399673.XSHE：创业版50
# print(example.describe())
# 部分数据绘制：调整为月收盘价 -> 完整绘制 -> 数据解读（可能的偏差）
sns.set()
plt.figure(figsize=(10,7))
sns.lineplot(data=example[:50])
plt.xticks(rotation=45)  # x轴标签倾斜45°
plt.tight_layout()  # 使图表大小与画板大小更加紧密贴合
# =========调整index为日期型=======
example.index=pd.to_datetime(example.index)
# 明确日期型，绘图时可以自动选择合适的周期进行绘制
# print(example.index)
plt.figure(figsize=(10,7))
sns.lineplot(data=example[:50])
plt.tight_layout()  # 使图表大小与画板大小更加紧密贴合
plt.show()
# 调整时间频率：日->月
bymonth=example.resample('M').first()
print(bymonth)
sns.lineplot(data=example)  # 按月度绘制收盘价趋势线
# ========计算、绘制涨跌幅=========
# 收益率、涨跌幅=（期末值-期中值）/期初值
print(bymonth.shift(1))  # 将原数据后移1行，作为期初值
byrate=(bymonth-bymonth.shift(1))/bymonth.shift(1)
print(byrate)
# * 方法2 *
byrate=bymonth.pct_change()
sns.relplot(data=byrate,kind='line')  # kind='line'表示折线图
plt.show()
# ========统一基点：初始值为1000，收盘价=基点*（1+涨跌幅）=============
bases=byrate
bases.iloc[0]=1000
bases.iloc[1:]=1+bases.iloc[1:]
bases=bases.cumprod()
print(bases)
sns.lineplot(data=bases)
plt.show()



