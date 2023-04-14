# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月14日
"""
import xlrd

# 打开表格
excel=xlrd.open_workbook('study.xlsx')
# print(excel)
# 获取工作簿
book=excel.sheet_by_name('学生手册')   # 按名称获取
print(book)
book=excel.sheet_by_index(0)  # 按索引获取
print(book)
for i in excel.sheets():
    print(i.name)  # 获取所有工作簿名称

print(book.nrows)  # 获取行数
print(book.ncols)  # 获取列数
for i in book.get_rows():
    # print(i)  # 获取每行对象
    content=[]
    for j in i:
        # print(j)  # 获取每行中每列的对象
        content.append(j.value)  # 获取每行中每列的值
    print(content)

