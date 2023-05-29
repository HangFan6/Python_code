# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月16日
"""
import pandas as pd
import scipy.stats
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize,stats

# print(help(scipy.optimize))  # 获取子级函数

'''创建拟合曲线：方程、计算拟合曲线、可视化'''
# # 创建方程=a*e^(-b*x)+c
# def y(x,a,b,c):
#     return a*np.exp(-b*x)+c
# xdata=np.linspace(0,4,50)  # 设置x坐标0~4中50个数据点
# ydata=y(xdata,2.5,1.3,0.5)
# ydata_noise=ydata+0.5*np.random.randn(xdata.size)
# # 生成拟合曲线: curve_fit
# # print(scipy.optimize.curve_fit(y,xdata,ydata_noise))
# params,pcov=optimize.curve_fit(y,xdata,ydata_noise)
# plt.plot(xdata,ydata_noise)
# plt.plot(xdata,y(xdata,*params))  #　*params＝params[0],params[1],params[2]
# plt.show()

'''随机变量与正态分布'''
# # *-创建随机变量：设置size、设置loc期望值、设置scale方差-*
# s1=stats.norm.rvs(loc=0,scale=1,size=10)
# # stats.norm：生成正态连续随机变量  rvs：随机变量样本
# # print(s1)
# sns.set()
# plt.figure(1) # 方法1
# sns.distplot(s1,bins=5)
# # 绘制分布曲线函数(正态)
# def normal(mean,std,color='pink'):
#     x=np.linspace(mean-4*std,mean+4*std,100)
#     p=stats.norm.pdf(x,mean,std)
#     z=plt.plot(x,p,color,linewidth=2)
#     return z
# plt.figure(2)  # 方法2
# sns.histplot(x=s1,stat='density')  # 绘制直方图
# normal(s1.mean(),s1.std())  # 分布图
# plt.show()

# # *-不同取值和方差的表现：均值决定中心位、方差决定高矮-*
# # 改动方差，观察变化
# s1=stats.norm.rvs(loc=0,scale=1,size=1000)
# s2=stats.norm.rvs(loc=0,scale=2,size=1000)
# s3=stats.norm.rvs(loc=0,scale=3,size=1000)
# plt.figure(1)
# for s in [s1,s2,s3]:
#     sns.distplot(s)
# plt.legend(labels=[1,2,3])
# # 改动均值，观察变化
# s1=stats.norm.rvs(loc=0,scale=1,size=1000)
# s2=stats.norm.rvs(loc=1,scale=1,size=1000)
# s3=stats.norm.rvs(loc=2,scale=1,size=1000)
# plt.figure(2)
# for s in [s1,s2,s3]:
#     sns.distplot(s)
# plt.legend(labels=[1,2,3])
# plt.show()

# # *-随机变量的数值特征：期望、方差，样本量越大越准确-*
# for s in [s1,s2,s3]:
#     print(s.mean(),s.std())


'''假设检验'''
# # 分布图：总体vs样本
# # 设置总体样本的概率分布
# mean0=72
# mean1=68
# std1=0.8
# s0=stats.norm.rvs(mean0,1,1000)
# s1=stats.norm.rvs(mean1,std1,100)
# plt.figure(1)
# sns.distplot(s0)
# sns.distplot(s1)
# plt.show()
#
# # 置信区间和拒绝域：a=0.05，概率p越小越能拒绝零假设
# # 置信区间：总体概率为95%
# plt.figure(2)
# sns.distplot(stats.norm.rvs(size=1000))  # 均值为0，方差为1
# sns.distplot(stats.norm.rvs(0,2,size=1000))  # 均值为0，方差为2
# plt.show()

# # 当类别数据>3*方差，基本上就是小概率时间，即：可以拒绝原假设
# # 拒绝域>3*std
# sns.distplot(stats.norm.rvs(size=1000))
# print(stats.norm.cdf(-2))  # 出现的数据小于-2 的概率
# print(stats.norm.ppf(0.025))  # 数据处于前0.025的水平的横坐标位置
# # 简单计算概率p值（z-score）
# mean0=72
# mean1=68
# std1=0.8
# s0=stats.norm.rvs(mean0,1,1000)
# s1=stats.norm.rvs(mean1,std1,100)
# zscore=(mean1-mean0)/std1
# print(zscore)  # 距离期望有多少个方差
# # 拒绝域>3*std  可以拒绝原假设


'''显著性检验'''
# # ====单样本检验====
# """
# 问：样本均值与标准t分布均值是否存在显著性差异
# 假设：a=0.05
# H0：不存在显著性差异
# H1：存在显著性差异
# """
# # 创建随机变量：t分布、自由度df
# sns.set()
# s0=stats.norm.rvs(size=1000)  # norm：标准正态分布
# s1=stats.t.rvs(20,size=1000)  # t：t分布，自由度20
# # # 自由度越高，越接近正态分布，反之越离散
# # sns.distplot(s0)
# # sns.distplot(s1)
# # plt.show()
#
# # 描述统计性：特征值
# # 偏度（skewness）：统计数据分布偏斜方向，是统计数据分布非对称程度的数字特征
# # 峰度（kurtosis）：概率密度分布曲线在平均值处峰值高低的特征数，如果峰度大于3，峰的形状比较尖
# # 方式1：调用统计函数
# print(s1.mean(),s1.var(),s1.max(),s1.min())  # 均值，方差，最大值，最小值
# # 方式2：调用describe
# print(stats.describe(s1))
#
# n,(smin,smax),sm,sv,sk,sr=stats.describe(s1)
# m,v,s,k=stats.t.stats(n-1,moments='mvsk')  # 自由度：n-1
# print(stats.t.stats(n-1,moments='mvsk'))  # 均值、方差、偏度、峰度
#
# # 计算t值（类别数据）、p值（概率）
# """
# 单总体t检验统计量为：t=(x~ - μ)/(δx/n^(1/2))
# 其中，i=1……n, x~ = sum(xi)/n为样本平均数，μ为均值，δx为标准差（=sqrt(方差)），
# s=(sum((xi - x~)^2)/n)^(1/2)为样本标准偏差，n为样本数。
# 该统计量t在零假说：μ=δ0为真的条件下服从自由度为n的分布
# """
# # 方式1：自己实现公式
# tv=(sm-m)/np.sqrt(sv/n)  # t值
# pv=stats.t.sf(np.abs(tv),n-1)*2  # 双边概率需*2
# print(tv,pv)
# # 方式2：调用ttest
# print(stats.ttest_1samp(s1,m))
# # t分布图
# t,p=stats.ttest_1samp(s1,m)
# sns.distplot(s1)
# sns.lineplot(x=[t,t],y=[0,0.4],color='red')
# plt.show()

# # ====双样本检验====
# # 创建随机变量：近似分布、不同分布
# size=1000
# s1=stats.norm.rvs(loc=5,scale=5,size=size)  # 正态分布 均值为5，方差为5 样本量
# s2=stats.t.rvs(20,loc=5,scale=5,size=size)  # t分布 自由度20 均值为5，方差为5 样本量
# s3=np.random.exponential(size=size)*5  # 指数分布（左偏分布）
# plt.figure(1)
# for s in [s1,s2,s3]:
#     sns.distplot(s)
# plt.legend(labels=['norm','t','exp'])
# plt.show()
# """
# ks检验：
#     一种基于累计分布函数的非参数检验
#     ks统计量：D=max|Fn(x)-F0(x)|，即样本所属总体的分布与给定给定分布之间的距离，越小越相同(差距小)
#     p值：根据D值找到对应类别数据并计算累计概率
# """
# # 双样本kstest：统计D、p值   （kstest 单样本）
# print(stats.ks_2samp(s1,s2))
# print(stats.ks_2samp(s1,s3))
# print(stats.ks_2samp(s2,s3))
# # 双样本ttest
# print(stats.ttest_ind(s1,s2))
# print(stats.ttest_ind(s1,s3))
# print(stats.ttest_ind(s2,s3))


# *********** 样本差异比较 *********
# 数据预处理：提取月消费
data=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
data.columns=['用户ID', '性别', '是否老人', '是否有伴侣', '是否有孩子',
       '在网时长', '通话服务', '多线程', '网络服务',
       '在线安全', '在线备份', '设备安全', '技术支持',
       '流媒体电视', '流媒体电影', '期限单位', '电子账单',
       '支付方式', '月消费', '总消费', '是否流失']
# print(data.head())
# 按是否流失进行分类：提取月消费
churn0=data[data['是否流失']=='No']['月消费']
churn1=data[data['是否流失']=='Yes']['月消费']
print(len(churn0),len(churn1))
plt.figure(1)
churn0.hist(bins=50)
churn1.hist(bins=50)
plt.legend(labels=['churn0','churn1'])
# 观察分布：频数分布、概率分布
rc = {'font.sans-serif': 'SimHei',   # SimHei表示黑体
      'axes.unicode_minus': False}   # 运行配置参数总的轴（axes）正常显示正负号（minus）
sns.set(rc=rc)
plt.figure(2)
sns.distplot(churn0)
sns.distplot(churn1)
plt.legend(labels=['churn0','churn1'])
plt.show()
# 双侧检验：是否存在显著性差异
# H0：非流失μ = 流失μ
# H1：非流失μ ≠ 流失μ
s0=churn0.tolist()  # 非流失
s1=churn1.tolist()  # 流失
print(stats.ks_2samp(s0,s1))  # p<<1‰，存在显著性差异，拒绝H0，接受H1
# 描述性统计
print(stats.describe(s0))
print(stats.describe(s1))
# 右侧检验：非流失用户月消费是否大于流失用户
# H0：非流失μ <= 流失μ
# H1：非流失μ > 流失μ
print(stats.ks_2samp(s0,s1,'greater'))  # 获得p值测试：s0>s1
# 结论：p值很小，s0>s1的判断拒绝,所以拒绝H1
print(stats.ks_2samp(s0,s1,'less'))  # 获得p值测试：s0<s1
# 结论：p=9%，s0<s1的判断不能拒绝,所以拒绝H1

# 按用户性别进行分类，提取月消费
# churn0: 男性用户
# churn1: 女性用户
churn0 = data[data['性别']=='Male']['月消费']
churn1 = data[data['性别']=='Female']['月消费']
# 双侧检验：是否存在显著性差异
# H0：男性用户μ = 女性用户μ，没有显著性差异
# H1：男性用户μ ≠ 女性用户μ
s0=churn0.tolist()  # 男性
s1=churn1.tolist()  # 女性
print(stats.ks_2samp(s0,s1))  # p=36.9%，不存在显著性差异，拒绝H1，接受H0

