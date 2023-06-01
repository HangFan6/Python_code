# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月30日
"""
from warnings import simplefilter
from sklearn import datasets
from sklearn import preprocessing as prep
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression  # 线性回归
import matplotlib.pyplot as plt
import seaborn as sns

simplefilter(action="ignore",category=FutureWarning)  # 忽略FutureWarning

# # 加载数据
# housing=datasets.load_boston()  # 导入波士顿房价数据
# # print(housing)
# housing.feature_names=['犯罪率', '住宅比例', '非住宅比例', '是否河道', '环保指数', '房间数', '自住比例', '就业中心距离',
#                        '高速可达性', '物业税', '学生教师比例', '黑人比例', '人口状况下降比']
# # 探索特征值
# print(housing.data.shape)  # 样本数、特征变量数
# house=pd.DataFrame(housing.data,columns=housing.feature_names)
# # print(house)
# # 回归预测模型：y=k*x+b
# model=LinearRegression()  # 确定要调用的模型
# x=housing.data[:,np.newaxis,5]  # np.newaxis将一维数组转换成二维数组
# y=housing.target
# model.fit(x,y)
# # 打印对应的公式系数
# print(model.score(x,y),model.coef_,model.intercept_)  # 相关性系数、斜率、截距
# # 绘制样本x、y
# plt.scatter(x,y)
# plt.plot(x,model.predict(x),color='r')
# plt.show()



# # =====数据预处理=========
# # * 标准化、归一化 *
# # 创建随机样本：分布差异 、统计概要、绘图
# data=pd.DataFrame({'a':np.random.exponential(3,1000),
#                    'b':np.random.normal(-5,0.5,1000),
#                    'c':np.random.normal(0,4,1000)})
# print(data.head())
# print(data.describe())
# plt.figure(1)
# sns.lineplot(data=data)
# plt.figure(2)
# sns.distplot(data['a'])
# sns.distplot(data['b'])
# sns.distplot(data['c'])
# plt.legend(['a','b','c'])
# plt.show()
# # ***********归一化：minmax  将所有数据统一到0~1的范畴**********
# # 方法1：直接调用sklearn.prep
# scaler1=prep.MinMaxScaler()  # 创建模型
# scaler1.fit(data)  # fit训练数据集
# print(scaler1.transform(data))  # 查看数据
# minmax1=pd.DataFrame(scaler1.transform(data),columns=['a','b','c'])
# print(minmax1.describe())
# plt.figure(3)
# sns.lineplot(data=minmax1)
# plt.figure(4)
# sns.distplot(minmax1['a'])
# sns.distplot(minmax1['b'])
# sns.distplot(minmax1['c'])
# plt.legend(['a','b','c'])
# plt.show()
# # 方法2：使用数学公式
# x=data
# minmax2=(x-x.min(axis=0))/(x.max(axis=0)-x.min(axis=0))
# print(minmax2.describe())
# print(minmax1.round(decimals=2)==minmax2.round(decimals=2))
# # *****标准化：zcore  形成0为均值，1为方差**********
# # 方式1：调用StandardScaler
# scaler2=prep.StandardScaler()
# scaler2.fit(data)
# print(scaler2.transform(data))
# scaler=pd.DataFrame(scaler2.transform(data),columns=['a','b','c'])
# print(scaler.describe())
# plt.figure(5)
# sns.lineplot(data=scaler)
# plt.figure(6)
# sns.distplot(scaler['a'])
# sns.distplot(scaler['b'])
# sns.distplot(scaler['c'])
# plt.legend(['a','b','c'])
# plt.show()



# # =========OneHot独热编码=============
# # * 自然编码 & 独热编码 *
# genders=['female','male']
# # 自然编码：0、1  -> female:0  male:1
# # 独热编码： -> female:[1,0]  male:[0,1]  from Europe:[0,0,1,0]
# locations=['from Africa','from Asia','from Europe','from US']
# browsers=['uses Chrome','uses Firefox','uses IE','uses Safari']
# # * 将定类特征转换为二进制 *
# # 创建模型 -> fit训练数据 -> transform显示数据 -> .attribute打印属性
# onehot=prep.OneHotEncoder(categories=[genders,locations,browsers],sparse=False,handle_unknown='ignore')
# # sparse=False:设置返回为数组，否则返回为矩阵  handle_unknown='ignore':当编码数据不存在时，编码值为0
# binary=onehot.fit_transform([['female','from Asia','uses Chrome'],
#                              ['male','from Canada','uses Safari']])
# print(binary)



# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# # ==========K-Means聚类算法===============
# # 生成数据：2个特征值、3个类别
# x,y=datasets.make_blobs(n_samples=500,centers=4,n_features=2)
# print(x.shape,y.shape)
# plt.figure(1)
# plt.scatter(x=x[:,0],y=x[:,1],c=y)
# plt.show()
# # kmeans聚类分析
# kms=KMeans(n_clusters=4)
# kms.fit(x)
# print(kms.cluster_centers_)  # 质心坐标
# print(kms.labels_)  # 类别标签
# y_pred=kms.fit_predict(x)  # 类别方式
# print(y_pred)
# plt.figure(2)
# plt.scatter(x=x[:,0],y=x[:,1],c=y_pred)
# plt.show()
# # 选择最优k值：轮廓系数
# plt.figure(3)
# for k in range(2,10):
#     y_pred = KMeans(n_clusters=k).fit_predict(x)  # 类别方式
#     score=silhouette_score(x,y_pred)
#     print('k值：',k,'轮廓系数值：',score)
#     plt.scatter(x=x[:, 0], y=x[:, 1], c=y_pred)
#     plt.show()



# from sklearn.datasets import load_iris  # 数据集
# from sklearn.neighbors import KNeighborsClassifier  # KNN估计器
# from sklearn.model_selection import train_test_split  # 数据集拆分
# from sklearn.metrics import classification_report  # 分析预测结果
# # ========KNN临近分类算法===========
# # 加载鸢尾花数据集
# iris=load_iris()
# # print(iris)
# x=iris.data  # 4个特征值
# y=iris.target  # 每个数据样本的所属类别
# x2d=x[:,:2]
# sns.set()
# sns.scatterplot(x2d[:,0],x2d[:,1],hue=y)
# plt.show()
# # 交叉验证：训练集和测试集
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)  # test_size设置测试数据占比
# print(x_train.shape,x_test.shape)
# # KNN算法
# knc=KNeighborsClassifier()  # 默认k=5
# knc.fit(x_train,y_train)  # 模型训练
# y_pred=knc.predict(x_test)  # 预测数据
# print(y_test,y_pred)
# # 评估KNN准确性
# scores=classification_report(y_test,y_pred,target_names=iris.target_names,output_dict=True)
# print(pd.DataFrame(scores))



from sklearn.model_selection import train_test_split  # 数据集拆分
# =========多元线性回归算法============
# 导入数据、回归 & 分类算法
data=datasets.load_boston()  # 结果集：.data房价影响因素 .target房价
# print(data)
x=pd.DataFrame(data.data,columns=data.feature_names)
y=pd.DataFrame(data.target,columns=['BostonPrice'])
# 数据集拆分：train、test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(x_train.shape,y_train.shape)
# 模型训练：LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
# 获取系数和截距：y=kx+b -> y=ax1+bx2+……+hx13+z     （系数：a、b、……、h  截距：z）
print(lr.coef_,lr.intercept_)
# 模型预测：预测值（y_pred） vs 真实值（y_test）
y_pred=lr.predict(x_test)  # 获取预测值
print(y_pred.shape,y_test.shape)
plt.figure(1)
plt.plot(np.arange(len(y_test)),y_test.values)
plt.plot(np.arange(len(y_test)),y_pred,color='r')
plt.legend(['real','predict'])
plt.show()
# 模型评估：MSE（均方误差）、数据量调整
from sklearn import metrics
res=metrics.mean_squared_error(y_test,y_pred)
print(res)








