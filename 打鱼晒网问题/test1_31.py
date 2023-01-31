# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年01月31日
"""
year = int(input("请输入查询Year："))
month = int(input("请输入查询Month："))
date = int(input("请输入查询Date："))


# 闰年规则：四年一闰,百年不闰,四百年再闰
# 判断闰年
def is_leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    else:
        return 0


# 计算从2000年到year-1年的天数
y_days = 0
for i in range(2000, year):
    if is_leapyear(i):
        y_days = y_days + 366
    else:
        y_days = y_days + 365
print(y_days)
# 计算year年1月到month月的天数
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leapyear(year) and month > 2:
    months[1] += 1
m_days = 0
for i in range(month-1):
    m_days = m_days + months[i]
print(m_days)
# 计算2000年1月1日 到 xx年xx月xx日 的天数
sum_all = y_days + m_days + date
print(sum_all)
# 计算小王打鱼还是晒网
x = sum_all % 5
if x in range(1, 4):
    print("打鱼去喽")
elif x == 0 or x == 4:
    print("晒网去喽")  # x=0或4
else:
    print("等一哈！让我看看是哪个角角出错啰！")
