# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月08日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # SimHei表示黑体
plt.rcParams['axes.unicode_minus'] = False  # 运行配置参数总的轴（axes）正常显示正负号（minus）

# ********   初识   *************
# # 创建figure、subplot
# # plt.subplots(2,1,sharex=True)  # 创建2行1列的图表画布,sharex:x轴一致
# plt.show()
# data=np.random.randn(100)  # 创建数据样本
# # print(data)
# fig,axs=plt.subplots(2,1)  # 创建子图
# axs[0].hist(data,bins=50,color='red')  # 在第1行图表中绘制  直方图
# axs[1].plot(data,color='green')  # 在第2行图表中绘制  折线图
# axs[0].set_title('正态分布')   # 参数设置  （单独一张图表时，参数设置可不加set_）
# axs[1].set_title('随机样本')
# axs[0].set_xlabel('value')
# axs[0].set_ylabel('freq')
# axs[1].set_xlabel('index')
# axs[1].set_ylabel('value')
# plt.show()   # 显示图表


# *********   可视化图表    ****************
# =========关联性===========
# x=np.random.randn(100)
# y=np.random.randn(100)*0.5+np.random.randn(1)
# # print(x,y)
# plt.scatter(x,y,color='r',marker='*')    # 散点图
# plt.xlim(-2,2)
# plt.ylim(-0.5,1)
# plt.grid()   # 显示网格
# # plt.show()

'''散点图'''
# data=pd.read_excel('order2019.xlsx')
# # print(data.describe())
# # print(data.columns)
# # ['id', 'orderID', 'userID', 'goodsID', 'orderAmount', 'payment','chanelID', 'platfromType', 'orderTime', 'payTime', 'chargeback']
#
# # 探索：商品均价 vs 销售数量的相关性
# types=data['goodsID'].unique().tolist()
# prices=[]
# amounts=[]
# for t in types:
#     price=data[data['goodsID']==t]['orderAmount'].mean()   # 价格中包括一些优惠，所以取均值
#     account=len(data[data['goodsID']==t])
#     prices.append(price)
#     amounts.append(account)
# # print(prices,amounts)
# # 绘制散点图
# plt.scatter(x=prices,y=amounts,color='g',marker='*')
# plt.title('商品价格 vs 数量')
# plt.xlabel('价格')
# plt.ylabel('数量')
# # 可通过xlim、xlim划分区间，判断相关性
# plt.grid()
# plt.show()
#
# # 随机比较和可视化3个商品的订单和销售情况
# prices=[]
# amounts=[]
# for t in ['PR000064','PR000582','PR000302']:
#     price=data[data['goodsID']==t]['orderAmount'].mean()   # 价格中包括一些优惠，所以取均值
#     account=len(data[data['goodsID']==t])
#     prices.append(price)
#     amounts.append(account)
# plt.scatter(x=prices[0],y=amounts[0],color='r',marker='*')
# plt.scatter(x=prices[1],y=amounts[1],color='g',marker='+')
# plt.scatter(x=prices[2],y=amounts[2],color='b')
# plt.title('商品价格 vs 数量')
# plt.xlabel('价格')
# plt.ylabel('数量')
# plt.grid()
# plt.show()

'''热力图'''
# # 工厂出货品质好坏
# factories=['fac1','fac2','fac3','fac4','fac5']
# quanlity=['bad','poor','general','good','great']
# result=np.round(np.random.random(25).reshape(5,5),1)
# fig,ax=plt.subplots(1,1)
# plt.imshow(result)
# # 轮流锁定单元格
# for i in np.arange(len(factories)):
#     for j in np.arange(len(quanlity)):
#         plt.text(j,i,result[i][j],color='w',ha='center',va='center')  # 标签文本设置
# # 设置坐标轴的类别数据标签
# ax.set_xticks(np.arange(len(quanlity)))
# ax.set_yticks(np.arange(len(factories)))
# ax.set_xticklabels(quanlity)
# ax.set_yticklabels(factories)
# ax.set_title('工厂的商品质量')
# fig.tight_layout()  # 设置图表分布
# plt.show()

'''直方图'''
# data=pd.read_excel('order2019.xlsx',sheet_name='data')
# print(data['orderAmount'].head())
# # 直方图：类别（数值）、频数（频率）
# plt.hist(data['orderAmount'],bins=1000)
# plt.xlim(data['orderAmount'].min(),5000)
# plt.show()
'''箱型图'''
# data=pd.read_excel('order2019.xlsx',sheet_name='data')
# # # 箱型图：单个变量、加入比较变量
# # plt.boxplot(data['orderAmount'])  # 箱体中的横线表示中位数
# # plt.ylim(0,2000)
# # plt.show()
# """
#     离群值>Q3+1.5*IQR, IQR=Q3-Q1
#     离群值<Q1-1.5*IQR, IQR=Q3-Q1
#     Q3:上四分位数；Q1:下四分位数
# """
# # 比较orderAmount和payment金额分布表现
# data2=data[['orderAmount','payment']]
# # print(data2)
# plt.boxplot(data2,showmeans=True,labels=data2.columns.tolist())  # showmeans显示均值
# plt.ylim(0,3000)
# plt.grid()
# plt.show()


'''折线图'''  '''堆叠面积图'''
# example=np.random.random(100)
# plt.figure(1)
# plt.plot(example,color='r')
#
# plt.fill_between(np.arange(100),y1=example,y2=0,alpha=0.5)  # alpha设置透明度
# plt.xlim(0,100)
# plt.ylim(0,1)
# plt.show()


# # *********股票数据示例*************
# dates=pd.date_range('20180101','20210101',freq='M')
# def get_price(size):
#     prices=np.cumsum(np.random.randn(size))
#     return prices
# size=len(dates)
# price1=get_price(size)
# price2=get_price(size)
# price3=get_price(size)
# fig=plt.figure(1)
# # =====方法1：分别绘制3条曲线
# # plt.plot(dates,price1)
# # plt.plot(dates,price2)
# # plt.plot(dates,price3)
# # fig.autofmt_xdate()  # 自动调整x轴标签显示方式，使其完整显示
# # =====方法2：将3条数据整合从dataframe，直接绘图
# data=pd.DataFrame([price1,price2,price3]).T
# data.index=dates
# data.plot()
# # plt.plot(data)
# # fig.autofmt_xdate()  # 自动调整x轴标签显示方式，使其完整显示
# # 创建未堆叠面积图
# plt.figure(2)
# plt.fill_between(dates,y1=price1,alpha=0.5)  # alpha设置透明度
# plt.fill_between(dates,y1=price2,alpha=0.5)
# plt.fill_between(dates,y1=price3,alpha=0.5)
# plt.show()


'''饼图'''
# 饼图简单示例
# pre=[0.1,0.2,0.3,0.4]
# plt.pie(pre,labels=['a','b','c','d'],explode=(0,0.2,0,0),autopct='%.1lf%%')
# # explode:对应图形剥离距离  autopct：显示数值占比
# plt.show()
'''条形图'''
# # 条形图简单示例
# data=[0.1,0.2,0.3,0.4]
# labels=['a','b','c','d']
# plt.bar(labels,data,color=['r','g','b','y'])
# # 设置数值标签
# for x,y in zip(labels,data):
#     plt.text(x,y/2,y)
# plt.show()

# 案例
# data=pd.read_excel('order2019.xlsx')
# # print(data.columns)
# # 计算各chanelID的payment总额
# data2=data[['chanelID','payment']]
# # print(data2)
# res=data2.groupby('chanelID').sum()
# # print(res)
# plt.figure(1)
# plt.figure(figsize=(10,10))  # 调整画板
# plt.pie(res['payment'],labels=res.index,autopct='%.1lf%%',shadow=True,textprops={'size':'smaller'})
# plt.show()  # 饼图
# fig=plt.figure(2)
# plt.bar(res.index,res['payment'])
# fig.autofmt_xdate()
# for x,y in zip(res.index.tolist(),res['payment'].tolist()):
#     plt.text(x,y,'{:g}'.format(y))  # '{:g}'.format(y)：科学计数法
# plt.show()  # 条形图

'''散点簇形图'''
# # 简单示例
# a_x=np.random.random(100)+1
# a_y=np.random.random(100)+1.5
# b_x=np.random.random(200)+2.1
# b_y=np.random.random(200)+1.7
# plt.scatter(a_x,a_y)
# plt.scatter(b_x,b_y)
# plt.show()

'''分组条形图'''
# # 简单示例
# x=['a','b','c','d']
# axis1=[1,2,3,4]
# axis2=[1.2,2.2,3.2,4.2]
# y1=[1,2,3,4]
# y2=[2,3,4,1]
# plt.bar(axis1,y1,width=0.2)
# plt.bar(axis2,y2,width=0.2)
# plt.show()

# # ************案例***************
# data=pd.read_excel('order2019.xlsx')
# chanels=data['chanelID'].unique().tolist()[:3]
# data2=data[(data['chanelID']==chanels[0]) | (data['chanelID']==chanels[1]) | (data['chanelID']==chanels[2])]
# # print(data2)
# res=data2.groupby(['chanelID','platfromType']).sum()
# # print(res)
# # x轴分组位置设置
# labels1=res.loc[chanels[0],:].index.tolist()
# labels2=res.loc[chanels[1],:].index.tolist()
# labels3=res.loc[chanels[2],:].index.tolist()
# fig,ax=plt.subplots(figsize=(8,7))
# plt.bar(np.arange(len(labels1))+1,res.loc[chanels[0],'payment'].tolist(),width=0.2)
# plt.bar(np.arange(len(labels2))+1.2,res.loc[chanels[1],'payment'].tolist(),width=0.2)
# plt.bar(np.arange(len(labels3))+1.4,res.loc[chanels[2],'payment'].tolist(),width=0.2)
# # x轴类别数据
# ax.set_xticks(np.arange(len(labels1)))
# ax.set_xticklabels(labels=labels1,rotation=45)
# plt.show()

'''发散型条形图'''   '''面积图'''
# 简单案例
# plt.hlines(y=['a','b','c'],xmin=0,xmax=[-1,2,0.5],colors=['r','g','b'])  # 发散型条形图
# plt.show()

data=pd.read_excel('order2019.xlsx')
res=data[['chanelID','payment']].groupby('chanelID').sum()
res=res.sort_values('payment')   # ascending默认为True，升序排序
res['colors']=['red' if x>10000000 else 'green' for x in res['payment']]
# print(res)
plt.figure(1)
plt.hlines(y=res.index,xmin=0,xmax=res['payment'],colors=res['colors'])   # 发散型条形图
plt.grid(linestyle='--',alpha=0.5)

res['error']=res['payment']-res['payment'].mean()  # 交易额差值排序
res=res.sort_values('chanelID')
plt.figure(2,figsize=(8,6))
plt.plot(res['error'])
plt.fill_between(res.index,res['error'],0,where=res['error']>0,facecolor='g',interpolate=True,alpha=0.5)
plt.fill_between(res.index,res['error'],0,where=res['error']<=0,facecolor='r',interpolate=True,alpha=0.5)
plt.xticks(rotation=45)
plt.show()


