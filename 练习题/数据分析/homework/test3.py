# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月06日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # SimHei表示黑体
plt.rcParams['axes.unicode_minus'] = False  # 运行配置参数总的轴（axes）正常显示正负号（minus）


'''test1'''
# data=np.random.randn(4,4)
# excel=pd.DataFrame(data,index=list('ABCD'),columns=list('OPKL'))
# print(excel)
# excel.plot()
# excel.plot(kind='barh')  # 横向条形图
# plt.show()


'''test2  人均寿命和人均国内生产总值的相关性'''
# data=pd.read_csv('WorldBank.csv')
# print(data)
# # print(data.columns)
# # ['Country', 'Continent', 'Life_expectancy', 'GDP_per_capita','Population']
# ages=data['Life_expectancy'].tolist()
# gdp=data['GDP_per_capita'].tolist()
# plt.scatter(x=gdp,y=ages,color='g',marker='*')
# plt.xlabel('GDP')
# plt.ylabel('life')
# plt.title('GDP vs life')
# plt.grid()
# plt.show()

'''test3  海南省海口市的天气热力图'''
# data=pd.read_excel('temperature.xlsx',sheet_name='Sheet1')
# week=data['海口（2021.1）'].tolist()
# weekdays=data.columns[1:8].tolist()
# print(week,weekdays)
# result=data[['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']].values
# print(result)
# print(type(result))
#
# fig, ax = plt.subplots(1, 1)
# plt.imshow(result)
# # 轮流锁定单元格
# for i in np.arange(len(week)):
#     index=0
#     for j in np.arange(len(weekdays)):
#         if index<=len(weekdays):
#             plt.text(j, i, 'NaN' if np.isnan(result[i][j]) else result[i][j], color='w', ha='center', va='center')
#             index += 1
#             continue
# # 设置坐标轴的类别数据标签
# ax.set_xticks(np.arange(len(weekdays)))
# ax.set_yticks(np.arange(len(week)))
# ax.set_xticklabels(weekdays)
# ax.set_yticklabels(week)
# ax.set_title('工厂的商品质量')
# fig.tight_layout()  # 设置图表分布
# plt.show()

'''test4 绘制一下人均GDP的直方图以及人均寿命的箱型图'''
# data=pd.read_csv('WorldBank.csv')
# plt.figure(1)
# plt.hist(data['GDP_per_capita'],bins=100,color='g')
# plt.xlim(0,50000)
# plt.title('人均GDP')
# plt.figure(2)
# plt.boxplot(data['Life_expectancy'])
# plt.ylim(45,85)
# plt.title('人均寿命')
# plt.xlabel('年龄')
# plt.show()

'''test5 统计每个大洲的国家个数'''
data=pd.read_csv('WorldBank.csv')
res=data.groupby('Continent').count()
res=res.sort_values('Country')
res.index=['大洋洲','南美洲','北美洲','亚洲','欧洲','非洲']
print(res)
plt.hlines(y=res.index,xmin=0,xmax=res['Country'],linewidth=15)
plt.show()








