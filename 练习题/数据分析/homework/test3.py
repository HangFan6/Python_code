# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年05月06日
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.random.randn(4,4)
excel=pd.DataFrame(data,index=list('ABCD'),columns=list('OPKL'))
print(excel)
excel.plot()
excel.plot(kind='barh')  # 横向条形图
plt.show()