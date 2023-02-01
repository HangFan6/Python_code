# -*- coding:utf-8 -*-
"""
作者：HET
题目：输出10-1000之间的素数，每行输出6个。并将素数写入d:/py/ab.txt
日期：2023年01月31日
"""
# 素数：除1和他本身，无法被其他数整除
# 写法1：
fp = open("d:/py/ab.txt", "w")
j = 0
list1 = []
for m in range(10, 1001):
    # flag = 0  # 表示是否存在素数
    for i in range(2, m):
        if m % i != 0:
            print(m, end=" ")
            j += 1
            list1.append(str(m))
            if j % 6 == 0:
                list1.append("\n")
            break
        else:
            break
print()
print(list1)
fp.writelines(list1)
fp.close()

# 写法2：
# fp = open("d:/py/ab.txt", "w")
# j = 0
# list1 = []
# for m in range(10, 1001):
#     flag = 0  # 表示是否存在素数
#     for i in range(2, m):
#         if m % i == 0:
#             flag = 0  # 不存在素数
#             # print(m)
#             break
#         else:
#             flag = 1
#     if flag == 1:
#         # m = str(m) + " "
#         # fp.write(m)  # 一行写入
#         print(m, end=" ")  # 输出素数
#         j += 1
#         list1.append(str(m))
#
#         if j % 6 == 0:
#             # print()
#             list1.append("\n")
# print()
# print(list1)
# fp.writelines(list1)
# fp.close()
