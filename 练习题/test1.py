# -*- coding:utf-8 -*-
"""
作者：HET
题目：企业发放的奖金根据利润提成。
    利润(I)低于或等于6万元时，奖金可提6%；
    利润高于6万元，低于19万元时，低于6万元的部分按10%提成，高于6万元的部分，可提成8.5%；
    19万到40万之间时，高于19万元的部分，可提成6%；
    40万到60万之间时高于40万元的部分，可提成5%；
    60万到100万之间时，高于60万元的部分，可提成3%；
    高于100万元时，超过100万元的部分按2%提成，
    从键盘输入当月利润I，求应发放奖金总数？
日期：2023年01月31日
"""
'''
分段计算：
不足6万元，利率0.06
高于6万元：
    6万元部分，利率0.1     6000元
    6~19：利率0.085       11050元
    19~40：利率0.06       12600元
    40~60：利率0.05       10000元
    60~100：利率0.03      12000元
    100以上：利率0.02
'''
profit = int(input("让我瞅瞅你这个月获得了好多利润："))
pft = [60000, 190000, 400000, 600000, 1000000]
rank = [60000, 130000, 210000, 200000, 4000000]
rate = [0.1, 0.085, 0.06, 0.05, 0.03, 0.02]
bonus = 0.0
if profit <= pft[0]:
    bonus += profit*0.06
    print("奖金为：%.2f" % bonus)
else:
    pft_max = []
    for i in range(5):
        if pft[i] < profit:  # pft[i]中 < profit 的元素下标为i
            pft_max.append(pft[i])
            bonus += rank[i]*rate[i]
            # 计算rank[i]及之前的奖金总和
            # print("奖金为：%.2f" % bonus)
    print(pft_max)
    profit = profit - max(pft_max)
    # print("奖金为：%.2f" % bonus)
    for i in range(len(pft_max)):
        if pft_max[i] == max(pft_max):
            bonus = bonus + profit * rate[i+1]
            print("奖金为：%.2f" % bonus)
