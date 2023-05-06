# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月05日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 创建数据样本
# （单样本）
df=np.random.randn(1000)  # 呈正态分布
df=pd.DataFrame(df,index=pd.date_range('20200101',periods=1000,))
print(df)
df.plot()  # 折线图
df['cumsum']=df.cumsum()
print(df)
df['cumsum'].plot()
pd.DataFrame(df.hist(bins=50))  # 直方图
plt.show()

# （多样本）
df2=pd.DataFrame(np.random.randn(1000,4),columns=list('ABCD'),index=pd.date_range('20200101',periods=1000))
df2=df2.cumsum()
df2.plot()
plt.show()


