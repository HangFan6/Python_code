# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月03日
"""
import numpy as np

# # ****** array ***********
# data=[[1,2,3,4],[5,6,7,8]]
# print(type(data))
# data=np.array(data)
# print(type(data))
# print(data.ndim)  # 维度
# print(data.shape)  # 形状

# # ****** arrange ***********
# print(range(15))   # 一维数组 range(0, 15)
# data=np.arange(15).reshape(3,5)  # 二维数组
# print(data)
#
# data2=np.zeros(10).reshape(2,5)
# print(data2)
# data3=np.zeros((2,5))
# print(data3)
#
# data4=np.ones((2,3,5))   # 三维数组
# print(data4)


# data=np.array([1,2,3,4,5])
# print(data.dtype)
# # 创建ndarray显示指定
# data2=np.array([1,2,3,4,5],dtype=np.float32)
# print(data2.dtype)
# data2[2]=6.58
# print(data2)

# data=np.array([1,2,3,4,5])
# data[1]=9.356
# data=data.astype(np.float32)
# print(data)


# data=np.array([1,2,3,4,5])
# print(data[3])   # 4
# print(data[-2])  # 4

# data=np.arange(14).reshape(2,7)  # 2行7列
# idx=data[0,3]  # 行、列下标从0开始
# print(idx)  # 3
# idx=data[0][3]
# print(idx)  # 3
# idx=data[0][-4]
# print(idx)  # 3

# data=np.arange(30).reshape(2,3,5)  # 2块3行5列
# print(data)
# idx=data[0,1,2]
# print(idx)
# idx=data[-1,2,-3]
# print(idx)


# *****切片***********
# data=np.array([1,2,3,4,5])
# print(data)
# x=data[0:3]  # 0<=x<3
# print(x)
# x=data[2:]  # 2<=x
# print(x)
# x=data[:-1]
# print(x)

# data2=np.arange(14).reshape(2,7)
# print(data2)
# x=data2[0:1,2:4]  # 行、列
# print(x)
# x=data2[1:,:5]  # 行、列
# print(x)

# data=np.arange(30).reshape(2,3,5)
# print(data)
# x=data[1:,2:,1:3]
# print(x)
# m=x[0][0][1]
# print(m)

# data=np.array([1,2,3,4,5])  # 一维数组
# lst=data[np.array([0,2,4])]
# print(lst)
# data2=np.arange(14).reshape(2,7)  # 二维数组
# lst=data2[np.array([0,1]),np.array([1,2])]
# print(lst)


# data=np.ones((10,10),dtype='int32')
# for i in range(1,9):
#     for j in range(1,9):
#         data[i][j]=0
# print(data)


# # =====数组运算===========
# a=np.random.random(10)*10
# b=np.random.random(10)*10
# print(a)
# print(b)
# x=np.add(a,b)
# print(x)
# x=np.subtract(a,b)
# print(x)
# x=np.multiply(a,b)
# print(x)
# x=np.divide(a,b)
# print(x)

# 三角函数
# ang=np.array([0,30,60,90,120,135,150,180])
# rad=np.sin(ang*np.pi/180)
# print(rad)

# 均值
# data=np.array([1,2,3,4,5])  # 一维数组
# print(data.mean())
# print(np.average(data))
# x=np.average(data,weights=np.array([1,1,1,2,3]))  # 加权
# print(x)
# data=np.array([1,2,3,4,5])  # 一维数组
# print(np.median(data))  # 中位数
# print(np.var(data))  # 方差
# print(np.std(data))  # 标准差

# data=np.array([1,2,3,4,5])  # 一维数组
# x=np.sum(data)
# print(x)
# x=np.prod(data)
# print(x)
# x=np.max(data)
# print(x)


# data=np.array([1,2,3,4,5])  # 一维数组
# x=np.where(data<4)
# print(x)  # 返回索引值，而非数值

# print(np.sort([4,2,6,9,1,8]))  # [1 2 4 6 8 9]


a=np.arange(12).reshape(3,4)
b=np.arange(12,24).reshape(3,4)
c=np.array([5,6,4,8])
print(np.dot(a,b.T))  # b.T 中T表示转置
x=np.dot(c,a.T)
print(x)



