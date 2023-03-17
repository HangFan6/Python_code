# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年03月11日
"""
from bs4 import BeautifulSoup  # 网页解析，用于数据获取
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取网页信息
import xlwt  # 操作Excel
# import sqlite3  # 进行数据库操作
import pymysql


def askUrl(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/99.0.4844.74 Safari/537.36"}
    req = urllib.request.Request(url=url, headers=header)  # 有时需要封装更多选项
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# =========利用正则表达式获取数据内容规则===================
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgScr = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S表示让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJidge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findIng = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
# findBd = re.compile(r'<p class="">(.*?)<br/>(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    # 调取页面信息
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 找到符合要求的字符串，形成列表
        for item in soup.find_all("div", class_="item"):  # class加下划线，表示是一个属性值
            # print(item)  # 测试 查看item中的所有信息
            data = []  # 保存一部电影的所有数据
            item = str(item)
            # 获取影片详情链接
            link = re.findall(findLink, item)[0]  # 使用re库通过正则表达式查找指定字符串
            data.append(link)
            imgScr = re.findall(findImgScr, item)
            data.append(imgScr)
            title = re.findall(findTitle, item)
            if (len(title) == 2):
                ctitle = title[0]
                data.append(ctitle)  # 添加中文名
                otitle = title[1].replace("/", "")  # 去除无关符号
                data.append(otitle)  # 添加外文名
            else:
                data.append(title[0])
                data.append(" ")
            rating = re.findall(findRating, item)
            data.append(rating)
            judgeNum = re.findall(findJidge, item)
            data.append(judgeNum)
            ing = re.findall(findIng, item)
            if len(ing) != 0:
                ing = ing[0].replace("。", "")  # 去掉句号
                data.append(ing)  # 添加概述
            else:
                data.append(" ")
            bd = re.findall(findBd, item)
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", str(bd))  # 去除<br/>
            bd = bd.replace(" ","").replace(r"['\n","").replace("']","").replace(r"\xa0"," ").replace(r"\n"," ")
            # print(bd)
            data.append(bd.strip())  # 去除前后空格
            datalist.append(data)  # 将处理好的电影信息放入列表中
    return datalist


def saveData(savepath, datalist):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('豆瓣电影250', cell_overwrite_ok=True)  # 创建工作表
    # worksheet.write(0,0,"hello")    # 行，列，内容
    col = ("电影详情链接", "图片链接", "中文名", "其他名称", "评分", "评价人数", "概况", "相关信息")  # 定义列名
    for i in range(0, 8):
        worksheet.write(0, i, col[i])  # 写入列名
    for i in range(0, 250):
        # print("第%d条"%i)
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i + 1, j, data[j])
    workbook.save(savepath)  # 保存数据表


def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = r".\test\豆瓣电影Top250.xls"  # 保存地址
    # askUrl(baseurl)
    datalist = getData(baseurl)
    saveData(savepath,datalist)     # excel表格保存


if __name__ == "__main__":
    main()
    print("爬取完毕！")
