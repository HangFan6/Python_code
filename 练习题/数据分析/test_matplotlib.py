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






