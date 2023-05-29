# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月17日
"""
import pandas as pd
import numpy as np
from scipy import optimize,stats
import seaborn as sns
import matplotlib.pyplot as plt

'''test1  利用scipy.optimize.curve_fit()进行正玄函数拟合'''
# # 拟合函数func：a * sin(b*x + c) + d
# def func(x,a,b,c,d):
#     return a * np.sin(b*x + c) + d
# xdata = np.linspace(0, 20, 100)
# ydata = func(xdata, -0.5, 1.0, 1.3, 0.5)
# ydata_noise = ydata + 0.2*np.random.randn(xdata.size)
# params,pcov=optimize.curve_fit(func,xdata,ydata_noise)
# plt.plot(xdata,ydata_noise)
# plt.plot(xdata,func(xdata,*params))
# plt.show()

'''test2 单样本t检验判断身高是否有显著性差异'''
"""
我国20-24岁男性的平均身高是171.9厘米，小慕对自己班级的男同学身高进行了统计，数据如下：
[169.63, 165.64, 161, 170.17 ,169.8, 174.94, 171.30, 180.8, 173.71, 166.37, 169.67 , 177.46, 169.88, 172.86, 177.29, 
171, 170.24, 175.19, 165.09, 169.43, 171, 167.71 , 172.72, 176, 160.26, 173.37, 179.63, 175.92, 179.59, 182]
并且运用t检验，对样本数据和20-24岁男性身高的总体均值进行显著差异性对比
"""
# # 20—24岁的男性平均身高是171.9厘米
# m = 171.9
# # 问题：样本均值与总体分布均值是否存在显著性差异？
# # 样本数据，单位：厘米
# sample = pd.array(
#     [169.63, 165.64, 161, 170.17, 169.8, 174.94, 171.30, 180.8, 173.71, 166.37, 169.67, 177.46, 169.88,172.86, 177.29,
#      171, 170.24, 175.19, 165.09, 169.43, 171, 167.71, 172.72, 176, 160.26, 173.37, 179.63, 175.92, 179.59, 182])
# # 查看样本值分布情况
# sns.distplot(sample)
# plt.show()
# # n:样本数量、sm:样本均值、sv:样本方差、sk:偏度、sr:峰度
# n, (smin, smax), sm, sv, sk, sr = stats.describe(sample)
# print(n, (smin, smax), sm, sv, sk, sr)
# # 零假设 H0：不存在显著差异
# # 备择假设 H1：存在显著差异
# # 计算t值（类别数据）、p值（概率）
# tv, pv = stats.ttest_1samp(sample, m)
# print(tv, pv)
# # 判断标准（显著差异），alpha=5%
# # p值<5%，拒绝零假设，备择假设成立
# if pv < 0.05:
#     print("存在差异显著")
# else:
#     print("不存在显著差异")
# # 结论
# # 概率大于0.05，小慕班级男生的身高与同年龄段的男性平均身高，不存在显著差异
# # 认为班级男生和20-24岁男生的身高状况相比没有异常


'''test3 KS检验判断两班客服的服务水平是否相同'''
"""
某公司客服部有两班次员工，各11人，双十一以来，每班次人员被投诉的情况如下表
第1班被投诉次数：2 0 7 1 1 0 1 2 1 2 4
第2班被投诉次数：3 5 4 0 2 3 0 7 4 4 6
用KS检验来判断一下两班次的服务水平吧，是否有显著性差异呢
"""
# s1=[2, 0, 7, 1, 1, 0, 1, 2, 1, 2, 4]
# s2=[3, 5, 4, 0, 2, 3, 0, 7, 4, 4, 6]
# for s in [s1,s2]:
#     sns.distplot(s)
# plt.legend(labels=[1,2])
# plt.show()
# # 零假设 H0：不存在显著差异
# # 备择假设 H1：存在显著差异
# # 计算D值（统计量）、p值（概率）
# st, pv = stats.ks_2samp(s1,s2)
# print(st, pv)
# # 判断标准（显著差异），alpha=5%
# # p值<5%，拒绝零假设，备择假设成立
# if pv < 0.05:
#     print("存在差异显著")
# else:
#     print("不存在显著差异")
# # 结论
# # 概率大于0.05，两班次的服务水平，不存在显著差异
# # 认为两班次的服务水平没有异常


'''test4 男性用户和女性用户的月消费额是否有显著性差异？'''



