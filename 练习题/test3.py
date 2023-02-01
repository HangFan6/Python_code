# -*- coding:utf-8 -*-
"""
作者：HET
题目：4、随机产生90个长度为5~25之间，由字母、数字、和“_”、“.”、“#”、“%”特殊字符组成的 字符串 构成列表，
找出列表中符合下列要求的 字符串：长度为10-22，必须以字母开头、可带数字、字母、“_”、“.”。
然后将列表中满足以下条件（大写字母、小写字母、数字和一些特殊符号'#','_','.'）的 字符串 写入文本d:/py/test.txt中。
日期：2023年02月01日
"""
import numpy as np
import random

# 生成上下限范围内定量的整数，上下限左闭右开，size=生成个数
# num = np.random.randint(0, 10, size=10)
# 生成0~9的数字ascii 左闭右开
num = np.arange(48, 58)
num_str = [chr(i) for i in num]
# print(num)

# 生成小写字母ascii
alp1 = np.arange(97, 123)
# print(real1)

# 生成大写字母表ascii
alp2 = np.arange(65, 91)
real2 = [chr(i) for i in alp2]

# 合并列表
all1 = [*num, *alp1, *alp2]
# print(all1)

# 根据ASCII将将int列表转换为str列表
all2 = [chr(i) for i in all1]
# print(all2)
ch = ['_', '.', '#', '%']
all_str = [*ch, *all2]
# print(all_str)

size_list = []  # 存放90个元素的字符串 长度 列表
list_1 = []  # 存放90个元素的字符串列表
i = 0
while i < 90:
    i += 1
    # 打乱列表
    np.random.shuffle(all_str)
    # print(all_str)
    # 取长度为5~25的随机数
    size = int(random.randint(5, 25))
    size_list.append(size)
    str1 = random.sample(all_str, size)
    # 将字符列表转换为字符串
    c = ''.join(str1)
    list_1.append(c)
    # print(str1)
    # print(c)
    # print(size)
print("随机产生的90个字符串元素列表为：\n%s" % list_1)
print(len(list_1))
# print(size_list)

list_2 = []  # 符合第二行要求的字符串列表
for i in range(0, 90):
    # list_1[i]中不含'#','%'的字符串
    if 10 < size_list[i] < 23 and list_1[i][0] in num_str and '%' not in list_1[i] and '#' not in list_1[i]:
        # print(list_1[i])
        list_2.append(list_1[i])
print("以数字开头，符合要求的字符串如下：\n%s" % list_2)
print()

# 将不含'%'的字符写入文件
pf = open("d:/py/test.txt", "w")
list_3 = []
for i in range(0, 90):
    # list_1[i]中不含%'的字符串
    if '%' not in list_1[i]:
        # print(list_1[i])
        # list_3.append(list_1[i])
        # pf.writelines(list_3)
        # 分行写入文件
        list_str = list_1[i] + '\n'
        list_3.append(list_str)
print('写入文件的数据为：\n%s' % list_3)
pf.writelines(list_3)
pf.close()
