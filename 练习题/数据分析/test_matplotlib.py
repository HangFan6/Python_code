# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月08日
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # SimHei表示黑体
plt.rcParams['axes.unicode_minus'] = False  # 运行配置参数总的轴（axes）正常显示正负号（minus）

# 创建figure、subplot
# plt.subplots(2,1,sharex=True)  # 创建2行1列的图表画布,sharex:x轴一致
# plt.show()
data=np.random.randn(100)  # 创建数据样本
print(data)
fig,axs=plt.subplots(2,1)  # 创建子图
axs[0].hist(data,bins=50,color='red')  # 在第1行图表中绘制  直方图
axs[1].plot(data,color='green')  # 在第2行图表中绘制  折线图
axs[0].set_title('正态分布')   # 参数设置  （单独一张图表时，参数设置可不加set_）
axs[1].set_title('随机样本')
axs[0].set_xlabel('value')
axs[0].set_ylabel('freq')
axs[1].set_xlabel('index')
axs[1].set_ylabel('value')
plt.show()   # 显示图表


