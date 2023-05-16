# -*- coding:utf-8 -*-
"""
作者：HET
    1、假设鸢尾花类型为目标值，那么鸢尾花特征值有几个？
    2、分析不同鸢尾花4个特征值的分布特性（提示：小提琴图、箱型图）
    3、分析不同鸢尾花pental_length和width的相关性（提示：散点图、回归图）
    4、分析不同鸢尾花之间的相关性/相似性（提示：热力图、配对图）
日期：2023年05月15日
"""
import seaborn as sns
import matplotlib.pyplot as plt

rc = {'font.sans-serif': 'SimHei',   # SimHei表示黑体
      'axes.unicode_minus': False}   # 运行配置参数总的轴（axes）正常显示正负号（minus）

iris=sns.load_dataset('iris',data_home=r'C:\Users\26915\seaborn-data',cache=True)
# print(iris)
# setosa是山鸢尾，versicolor是杂色鸢尾，virginica弗吉尼亚鸢尾
cols=iris.columns[:-1]
print('鸢尾花特征值有%d个'%len(cols))
species=['setosa','versicolor','virginica']
sns.set(rc=rc)
'''分布特性'''
i=50
for c in species:
      plt.figure(1)
      sns.violinplot(data=iris[:i])  # 小提琴图
      plt.title('%s鸢尾花4个特征值的分布特性'%c)
      plt.figure(2)
      sns.boxplot(data=iris)   # 箱型图
      plt.title('%s鸢尾花4个特征值的分布特性'%c)
      plt.show()
      i += 50
'''相关性'''
plt.figure(1)
sns.scatterplot(data=iris,x='petal_length',y='petal_width',hue='species')  # 散点图
plt.figure(2)
sns.lmplot(data=iris,x='petal_length',y='petal_width',hue='species')  # 回归图
plt.show()
'''相关性/相似性'''
corrs=iris.corr()  #　计算相关性指数
plt.figure(1)
sns.heatmap(corrs,annot=True,cmap='YlGnBu')   # 热力图
plt.figure(2)
sns.pairplot(iris,hue='species')   # 配对图
plt.show()
