# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月30日
"""
import sklearn as sk
from warnings import simplefilter
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

simplefilter(action="ignore",category=FutureWarning)  # 忽略FutureWarning
# 加载数据
housing=datasets.load_boston()  # 导入波士顿房价数据
# print(housing)
housing.feature_names=['犯罪率', '住宅比例', '非住宅比例', '是否河道', '环保指数', '房间数', '自住比例', '就业中心距离',
                       '高速可达性', '物业税', '学生教师比例', '黑人比例', '人口状况下降比']
# 探索特征值
print(housing.data.shape)  # 样本数、特征变量数
house=pd.DataFrame(housing.data,columns=housing.feature_names)
# print(house)
# 回归预测模型：y=k*x+b
model=LinearRegression()  # 确定要调用的模型
x=housing.data[:,np.newaxis,5]  # np.newaxis将一维数组转换成二维数组
y=housing.target
model.fit(x,y)
# 打印对应的公式系数
print(model.score(x,y),model.coef_,model.intercept_)  # 相关性系数、斜率、截距
# 绘制样本x、y
plt.scatter(x,y)
plt.plot(x,model.predict(x),color='r')
plt.show()







