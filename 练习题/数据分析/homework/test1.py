# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月04日
"""
import numpy as np

"""
1、NumPy创建三个数组，分别用于记录5个长方体的长、宽、高
2、每个长方体的长、宽、高数据如下：
    长：5, 6, 9, 50, 20
    宽：3, 3, 8, 25, 10
    高：2, 2, 5, 18, 8
3、计算每个长方体的体积
"""
# length=np.array([5, 6, 9, 50, 20])
# width=np.array([3, 3, 8, 25, 10])
# height=np.array([2, 2, 5, 18, 8])
# print(np.multiply(np.multiply(length,width),height))
# size=[]
# for i in range(0,5):
#     x=length[i]*width[i]*height[i]
#     size.append(x)
# print(size)

"""
计算成交量加权平均价格（VWAP）
以下是某只股票连续一个月的收盘价与成交量，运用所学知识计算一下成交量加权平均价格吧
收盘价：
[36.1,39.32,45.03,34.32,33.44,46.5,51.88,55.2,58.16,54.54,56.85,59.18,59.9,63.13,58.3,50.56,38.61,42.62,42.88,48.16,
53.21,49.31,52.12,59.56,60,55.36,55.76,52.47,46.67,51.99]
成交量：
[144800,473000,236800,42600,64100,494200,322100,608500,240800,162400,127500,86200,149000,184100,949000,144500,162200,
994700,853500,572000,395400,290300,521000,885200,188000,504300,718000,192700,138800,824200]
"""
# price=np.array([36.1,39.32,45.03,34.32,33.44,46.5,51.88,55.2,58.16,54.54,56.85,59.18,59.9,63.13,58.3,50.56,38.61,42.62,42.88,48.16,
# 53.21,49.31,52.12,59.56,60,55.36,55.76,52.47,46.67,51.99])
# num=np.array([144800,473000,236800,42600,64100,494200,322100,608500,240800,162400,127500,86200,149000,184100,949000,144500,162200,
# 994700,853500,572000,395400,290300,521000,885200,188000,504300,718000,192700,138800,824200])
# result=np.average(price,weights=num)
# print(result)



# arr=np.arange(1, 13).reshape(4, 3)
# print(arr)
# num_add=np.sum(arr)
# print(num_add)
# column=[]
# row=[]
# for i in range(1,4):
#     h=arr[:,i-1:i]
#     column.append(np.sum(h))
# print(column)  # 列
# for i in range(1,5):
#     l=arr[i-1:i,:]
#     row.append(np.sum(l))
# print(row)  # 行
# print(np.max(arr))
# print(np.min(arr))
#
# column=np.sum(arr,axis=0)  #列
# print(column)
# row=np.sum(arr,axis=1)  # 行
# print(row)

"""
有一个酒鬼，他就是小慕，酒鬼小慕最初停留在原点的位置，每走一步时，
方向是不确定的，在经过一定时间之后，我们希望计算出酒鬼小慕与原点的距离。
假设酒鬼小慕走了2000步（每步0.5米），向前走一步记为1，向后走一步记为-1，
当计算距原点的距离时，就是将所有的步数进行累计求和。
"""
step=np.random.randint(0,high=2,size=2000)
step=np.where(step==0,-1,1)
print(step)
length=np.cumsum(step)*0.5
print(length)  # 每步距离
print(max(length))  # 正向最远
print(min(length))  # 反向最远
x=0
for i in range(2000):
    x+=1
    if length[i]>=15:
        print("小慕距原点距离大于或等于15米时，共走了%s步"%x)
        break
    if x==2000:
        print("小慕最远没有走到15米")




