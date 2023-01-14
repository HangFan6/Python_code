# 和风天气
import requests
import csv
import numpy as np
import pandas as pd
from sklearn import linear_model
# from scipy.interpolate import make_interp_spline    # 借助插值方法，来对x坐标数组和y坐标数组进行插值，使折线图变平滑
from bs4 import BeautifulSoup   # 可以从HTML或XML文件中提取数据
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # SimHei表示黑体
plt.rcParams['axes.unicode_minus'] = False  # 运行配置参数总的轴（axes）正常显示正负号（minus）

time = input("请选择查询天气的日期(now or 7d)：")
# now：实时天气，7d：连续7天天气情况（与实时天气json输出有区别）
api_weather = 'https://devapi.qweather.com/v7/weather/' + str(time) + '?location={}&key={}&output_format={}'    # 实时天气
# api_weather = 'https://devapi.qweather.com/v7/weather/7d?location={}&key={}&output_format={}'   # 7天天气 , 3d = 3天天气
key = '30af70fc27614f6ab495d411a59ac894'
# location = 101040200
city_ZH = input("请输入要查询的地点:")
fp = 'China-City-List_update_by_2021-11-29.csv'
with open(fp, 'rt', encoding='gbk') as amap_adcode_fn:
    amap_adcode = csv.reader(amap_adcode_fn)
    for tmp in amap_adcode:
        # print(tmp)
        if city_ZH in tmp[2]:
            # print(tmp[0], tmp[2])
            location = tmp[0]
            print(location)
output_format = 'json'
url1 = api_weather.format(location, key, output_format)
print(url1)
# import pprint
response = requests.get(url1).json()
# print(response)

# ======获取24h天气情况=====================================================
api_24h = 'https://devapi.qweather.com/v7/weather/24h?location={}&key={}&output_format={}'
# key = '30af70fc27614f6ab495d411a59ac894'  # 开头已写
# location = 101230201  # 厦门
# output_format = 'json'
url_24h = api_24h.format(location, key, output_format)
print(url_24h)
response_24h = requests.get(url_24h).json()
weather_24h = response_24h['hourly']
print(weather_24h)

fxTime_24h = []
temp_24h = []
windSpeed_24h = []
for x in range(0, 24):
    weather_24h = response_24h['hourly'][x]
    temp_h = weather_24h.get('temp')
    fxTime_h = weather_24h.get('fxTime')
    windSpeed_h = weather_24h.get('windSpeed')
    temp_24h.append(temp_h)
    fxTime_24h.append(fxTime_h)
    windSpeed_24h.append(windSpeed_h)
# print(temp_24h)
# print(fxTime_24h)
# 将型为'2023-01-03T23:00+08:00'的时间格式转换为整点时间'23'
fxTime_R = []
for i in range(0, len(fxTime_24h)):
    x = fxTime_24h[i][fxTime_24h[i].find('T') + 1:]
    fxTime_R.append(x)
fxTime_L = []
for i in range(0, len(fxTime_24h)):
    y = fxTime_R[i][:fxTime_R[i].find('+') - 3]
    fxTime_L.append(y)
print(fxTime_L)

if time == 'now':
    # 显示当前天气
    weather_now = response['now']
    print(weather_now)

    # 天气播报方式：英文转中文
    zh_to_en_1 = {
        "数据观测时间": "obsTime",
        "温度": "temp",
        "体感温度": "feelsLike",
        "图标代码": "icon",
        "天气": "text",
        "风向360角度": "wind360",
        "风向": "windDir",
        "风力等级": "windScale",
        "风速(公里/小时)": "windSpeed",
        "相对湿度": "humidity",
        "当前小时累计降水量(毫米)": "precip",
        "大气压强(百帕)": "pressure",
        "能见度(公里)": "vis",
        "云量": "cloud",
        "露点温度": "dew"
    }
    # for key, value in weather_now.items():  # for key in weather_now.items():
    #         print(key, ':', value)  # print(key, ':', weather_now[key])
    # # pprint.pprint(response)
    for key, value in zh_to_en_1.items():
        print(key, ":", weather_now[value])
    print()

    # ==========24h温度变化折线图=====================
    x = fxTime_L
    # plt.figure(1)
    temp_24h = [int(i) for i in temp_24h]  # 将温度的字符类型转为数值类型list (可替换为下一行表达式)
    # temp_24h = np.array(temp_24h).astype(int)  # -> [ 8  8  9  9 13 15 13]型
    plt.plot(x, temp_24h, color='red', label='temp_24h', marker='^')
    plt.xticks(x)
    plt.title(str(city_ZH) + '今日24h温度变化图')
    plt.xlabel('时间/h')
    plt.ylabel('摄氏度/℃')
    plt.show()

    # ====24h温度曲线图（未完成）====
    # n = len(x)
    # xd = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,]
    # x1 = np.array(xd)
    # y1 = np.array(temp_24h)
    # pic_name = str(city_ZH) + '今日24h温度变化曲线图'
    # plt.rcParams['figure.figsize'] = (10 * 16 / 9, 10)
    # plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    # # 对x1和y1进行插值
    # x_smooth = np.linspace(x1.min(), x1.max(), 50)
    # y_smooth = make_interp_spline(x1, y1)(x_smooth)
    # plt.plot(x_smooth, y_smooth)   # 显示平滑曲线
    # plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    # plt.legend()
    # plt.show()

# =======================天气灾害预警========================================================
    # ====方法1：直接根据网站灾害预警api获取=============
    api_warning = 'https://devapi.qweather.com/v7/warning/now?location={}&lang=zh&key={}&output_format ={}'
    key = '30af70fc27614f6ab495d411a59ac894'  # 开头已写
    # location = 101230201  # 厦门
    # output_format = 'json'
    url_warning = api_warning.format(location, key, output_format)
    print(url_warning)
    response_1 = requests.get(url_warning).json()
    print(response_1)
    response_warn = response_1['warning']
    # if response_warn == []:
    #     print("未来暂无极端天气")
    # else:
    #     response_warn = response['warning'][0]
    #     print(response_warn)
    #     warning_text = response_warn['text']  # 预警内容
    #     print(warning_text)
    #     warning_pub = response_warn['pubTime']  # 发布时间
    #     warning_start = response_warn['startTime']  # 可能为空
    #     warning_end = response_warn['endTime']  # 可能为空
    #     warning_severity = response_warn['severity']  # 预警严重等级
    #     warning_sev_Color = response_warn['severityColor']  # 预警严重等级颜色，可能为空
    #     warning_typeName = response_warn['typeName']  # 预警类型名称
    #     warning_urgency = response_warn['urgency']  # 预警紧迫程度，可能为空
    # =====方法2：根据获取的未来天气数据，自行设置预警类型和值================
    # ======风级预警信号（为更好的展示效果，未按标准等级计算）====
    windSpeed_24h_ave = sum([int(i) for i in windSpeed_24h]) / 24
    wind = ["大风：折断树枝", "疾风：步行困难", "强风：电线有声", "和风：吹起尘土", "微风：旌旗展开"]
    result = ""
    if windSpeed_24h_ave >= 10:
        result = wind[0]
    elif windSpeed_24h_ave >= 8:
        result = wind[1]
    elif windSpeed_24h_ave >= 6:
        result = wind[2]
    elif windSpeed_24h_ave >= 4:
        result = wind[3]
    elif windSpeed_24h_ave >= 2:
        result = wind[4]
    else:
        print()
    print(result)

    # ===数据可视化，将实时天气以图像方式展示========
    img_id = weather_now.get('icon')
    img_id += '.png'
    # plt.figure()
    fig = plt.figure()  # 创建一个全局绘图区域

    sunny_fp = img_id  # 天气情况图片
    sunny_img = plt.imread(sunny_fp, format='png')
    ax2 = fig.add_axes([0.25, 0.3, 0.8, 0.7])
    ax2.imshow(sunny_img)
    ax2.axis('off')
    # 天气主图文字
    temp = weather_now.get('temp')
    text = weather_now.get('text')
    windDir = weather_now.get('windDir')
    ax = fig.add_subplot(111)
    ax.text(-0.2, 2, "天气预报" + "  " + str(city_ZH), fontsize=25)
    ax.text(-0.2, 1.3, "天气：" + text + '\n'
            + "温度：" + temp + r'$^o$C' + '\n'
            + "风向：" + windDir + '\n', fontsize=20)
    ax.text(-0.2, 1.2, result, fontsize=20)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.axis('off')
    plt.show()
    # =============向QQ邮箱发送信息========================================
    import ssl
    # import requests
    # import requests
    # import json
    # from flask import jsonify
    # from flask import Flask, request
    # # smtplib 用于邮件的发信动作
    import smtplib
    # # email 用于构建邮件内容
    # from email.mime.text import MIMEText
    # # 构建邮件头
    # from email.header import Header
    from email.message import EmailMessage
    # # import schedule
    # import time
    # from threading import Timer

    # 这里我调用接口了，如果不调用 可以直接删除
    # url_a = ''
    # 无需安装第三方库SMTP服务
    key2 = '授权码'  # 换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
    email_address = '邮箱@qq.com'  # 换成你的邮箱地址
    email_password = key2
    # smtp = smtplib.SMTP('smtp.qq.com', 25)
    context = ssl.create_default_context()
    sender = email_address  # 发件邮箱
    receiver = ['邮箱@qq.com']
    # 收件邮箱

    subject = "天气预报推送"  # 主题
    # 这里我调用了自己的接口，如果不需要直接将body改为 body = '正文'
    # body = requests.get(url_a).text
    if len(response_warn) == 0:
        print("未来暂无极端天气")
        body = '主子！我又来了！\n' + \
               '愿你每天开开心心！\n' + \
               str(city_ZH) + '近日天气如下：\n' + \
               '天气更新时间为：' + response['updateTime'] + '\n' + \
               '天气：' + weather_now.get('text') + '\n' + \
               '温度：' + weather_now.get('temp') + '°C' + '\n' + \
               '风向：' + weather_now.get('windDir') + '\n' + \
               '风力：' + weather_now.get('windScale') + '级\n' + \
               '风速：' + weather_now.get('windSpeed') + '公里/小时\n'
    else:
        warning = response_1['warning'][0]
        warning_text = warning['text']  # 预警内容
        # print(warning_text)
        body = '主子！我又来了！\n' + \
               '愿你每天开开心心！\n' + \
               str(city_ZH) + '近日天气如下：\n' + \
               '天气更新时间为：' + response['updateTime'] + '\n' + \
               '天气：' + weather_now.get('text') + '\n' + \
               '温度：' + weather_now.get('temp') + '°C' + '\n' + \
               '风向：' + weather_now.get('windDir') + '\n' + \
               '风力：' + weather_now.get('windScale') + '级\n' + \
               '风速：' + weather_now.get('windSpeed') + '公里/小时\n' + \
               '天气预警：' + warning_text

    msg = EmailMessage()
    msg['subject'] = subject  # 邮件主题
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)  # 邮件内容

    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

if time == '7d':
    zh_to_en_2 = {
        "观测日期": "fxDate",
        "日出": "sunrise", "日落": "sunset",
        "月出": "moonrise", "月落": "moonset",
        "月相": "moonPhase", "月相图标": "moonPhaseIcon",
        "最高温度": "tempMax", "最低温度": "tempMin",
        "白天天气图标": "iconDay", "白天天气": "textDay",
        "晚上天气图标": "iconNight", "晚上天气": "textNight",
        "白天360度风向": "wind360Day", "白天风向": "windDirDay",
        "白天风力等级": "windScaleDay", "白天风速(公里/小时)": "windSpeedDay",
        "晚上360度风向": "wind360Night", "晚上风向": "windDirNight",
        "晚上风力等级": "windScaleNight", "晚上风速(公里/小时)": "windSpeedNight",
        "相对湿度": "humidity",
        "当前小时累计降水量(毫米)": "precip",
        "大气压强(百帕)": "pressure",
        "能见度(公里)": "vis",
        "云量": "cloud",
        "紫外线指数": "uvIndex"
    }
    # print(response['daily'])

    for weather_daily in response['daily']:
        print(weather_daily)
        # for key, value in weather_daily.items():
        #         print(key, ':', value)
        print()
        for key, value in zh_to_en_2.items():
            print(key, ":", weather_daily[value])

    # # =================================================================================================
    # # 将未来7天（含今天）的天气情况的键值转换为列表，并输出表格的形式
    # # day_sign的设置可以对应选择白天或晚上的天气数据
    # Date, sunrise, sunset, moonrise, moonset, moonPhase, moonPhaseIcon, temp, \
    #     icon, text, wind360, windDir, windScale, windSpeed, \
    #     humidity, precip, pressure, vis, cloud, uvIndex, \
    #     day_sign = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    # for i in range(0, 7):
    #     if i < 7:
    #         d = response['daily'][i]
    #         # print(d)
    #         sub_data = list(d.values())
    #         # print(sub_data)
    #
    #         # Date   天气更新时间
    #         Date.append((sub_data[0]) + ' 11:00:00')
    #         Date.append((sub_data[0]) + ' 23:00:00')
    #         # text
    #         text.append(sub_data[10])
    #         text.append(sub_data[12])
    #         # temp
    #         temp.append(sub_data[7])
    #         temp.append(sub_data[8])
    #         # # tempMin
    #         # tempMin.append(sub_data[8])
    #         # tempMin.append(sub_data[8])
    #         # windDir
    #         windDir.append(sub_data[14])
    #         windDir.append(sub_data[18])
    #         # windScale
    #         windScale.append(sub_data[15]+'级')
    #         windScale.append(sub_data[19]+'级')
    #         # day_sign
    #         day_sign.append(1)  # 白天天气
    #         day_sign.append(0)  # 夜晚天气
    #
    # future_data = pd.DataFrame({'Date': pd.to_datetime(Date, format='%Y-%m-%d %H:%M:%S'),
    #                             'day_sign': day_sign,
    #                             'text': text,
    #                             'temp': temp,  # np.array(temp, dtype=np.int64)将temp规范成为整形变量
    #                             'windDir': windDir,
    #                             'windScale': windScale})
    # # print(future_data)    # 输出为数据表
    # # ===============================================================================================

    # =========将数据保存到csv中，并使1-2不会转换成1月2日============================
    # import pandas as pd
    # df = pd.DataFrame({'d': ['1-2', '2-3']})
    # df['d'] = df['d'].apply(lambda x: '\t' + x)
    # df.to_csv('t0309.csv')

# ==========将7天的天气所有数据保存到weather-of-7days.csv表格中======================
    """保存为csv文件"""
    with open('weather-of-7days.csv', 'w', encoding='gbk', newline='') as f:
        header = ['fxDate', 'sunrise', 'sunset', 'moonrise', 'moonset', 'moonPhase', 'moonPhaseIcon', 'tempMax',
                  'tempMin', 'iconDay', 'textDay', 'iconNight', 'textNight', 'wind360Day', 'windDirDay',
                  'windScaleDay', 'windSpeedDay', 'wind360Night', 'windDirNight', 'windScaleNight',
                  'windSpeedNight', 'humidity', 'precip', 'pressure', 'vis', 'cloud', 'uvIndex']
        data = response['daily']
        f_csv = csv.DictWriter(f, fieldnames=header)
        f_csv.writeheader()
        f_csv.writerows(data)

    # 打开并读取之前保存的7天的天气所有数据（weather-of-7days.csv表格）
    gp = 'weather-of-7days.csv'
    # data = pd.read_csv(gp, usecols=['fxDate', 'tempMax', 'tempMin'])
    # print(data)

    with open(gp, 'r', encoding='gbk') as m:
        reader = csv.reader(m)
        # writer = csv.writer(m, quoting=csv.QUOTE_ALL)
        header_row = next(reader)
        fxDate, tempMax, tempMin, wind360Day, windDirDay, windScaleDay, windSpeedDay, wind360Night, windDirNight, \
            windScaleNight, windSpeedNight, textDay, data = [], [], [], [], [], [], [], [], [], [], [], [], []
        for row in reader:
            fxDate.append(row[0])
            tempMax.append(row[7])
            tempMin.append(row[8])
            wind360Day.append(row[13])
            windDirDay.append(row[14])
            windScaleDay.append(row[15])
            windSpeedDay.append(row[16])
            wind360Night.append(row[17])
            windDirNight.append(row[18])
            windScaleNight.append(row[19])
            windSpeedNight.append(row[20])
            textDay.append(row[10])

        data.append(fxDate)
        data.append(tempMax)
        data.append(tempMin)
        data.append(wind360Day)
        data.append(windDirDay)
        data.append(windScaleDay)
        data.append(windSpeedDay)
        data.append(wind360Night)
        data.append(windDirNight)
        data.append(windScaleNight)
        data.append(windSpeedNight)
        data.append(textDay)
        print(data)
        # print(data[1])  # -> ['17', '16', '18', '20', '21', '17', '20']型
# =============================高低温折线图数==============================================
        # 高低温折线图数据整理
        tempMax_list = [int(i) for i in data[1]]  # 最高温度数据list
        # 简单写为 tempMax_list = data[1]
        # ======上式可理解为：===========
        # tempMax_list = []
        # for i in data[1]:
        #     tempMax_list.append(i)
        # print(tempMax_list)
        # =============================
        tempMin_list = [int(i) for i in data[2]]  # 最低温度数据list
        # print(tempMax_list)    # ['8', '8', '9', '9', '13', '15', '13']型 -> [8, 8, 9, 9, 13, 15, 13]型
        # print(np.array(data[1], dtype=np.int64))  # -> [ 8  8  9  9 13 15 13]型
    # ===========================================================
    # 只能输出一列的数据到list列表中
    # with open(gp, 'r', encoding='utf-8') as m:
    #     fxDate = [row['fxDate'] for row in reader]
    #     tempMax = [row['tempMax'] for row in reader]
    #     tempMin = [row['tempMin'] for row in reader]
    # print(tempMax)
    # print(tempMin)
    # ==========================================================
        tempMax_ave = sum(tempMax_list) / 7  # 求平均高温
        tempMin_ave = sum(tempMin_list) / 7  # 求平均低温
        # print("%.1f" % tempMax_ave)  # 平均高温保留两位小数
        tempMax_y = max(tempMax_list)   # 求最高温度
        # print(tempMax)
        # print(tempMax_y)
        tempMax_x = tempMax_list.index(tempMax_y)+1  # 使图表表示时下标从1开始
        tempMin_y = min(tempMin_list)  # 求最低温度
        # print(tempMin)
        # print(tempMin_y)
        tempMin_x = tempMin_list.index(tempMin_y) + 1

        # 高低温数据可视化
        x = range(1, 8)
        plt.figure(1)
        plt.plot(x, tempMax_list, color='red', label='高温', marker='^')  # 画出高温度曲线
        plt.plot(x, tempMin_list, color='blue', label='低温', marker='^')  # 画出低温度曲线
        plt.scatter(x, tempMax_list, color='red')  # 点出高温每个时刻的温度点
        plt.scatter(x, tempMin_list, color='blue')  # 点出低温每个时刻的温度点
        plt.plot([1, 8], [tempMax_ave, tempMax_ave], c='black', linestyle='--')  # 画出平均高温温度虚线
        plt.plot([1, 8], [tempMin_ave, tempMin_ave], c='black', linestyle='--')  # 画出平均低温温度虚线
        plt.legend()
        # 标出最高温度、最低温度
        plt.text(tempMax_x + 0.15, tempMax_y + 0.15, str(tempMax_y), ha='center', va='bottom', fontsize=10.5)
        plt.text(tempMin_x + 0.15, tempMin_y + 0.15, str(tempMin_y), ha='center', va='bottom', fontsize=10.5)
        plt.xticks(x)
        plt.title(str(city_ZH)+'未来7天高温低温变化曲线图')
        plt.xlabel('未来天数/天')
        plt.ylabel('摄氏度/℃')
        # plt.savefig('image/{}15天温度曲线.png'.format(city_name), bbox_inches='tight')
        plt.show()

# ============================风级雷达图=============================================
        # =======（风级雷达图）数据处理=========
        fxDate_list = data[0]   # 日期
        wind360Day_list = data[3]   # 风向
        wind360Night_list = data[7]
        windScaleDay_list = data[5]   # 风级
        windScaleNight_list = data[9]
        windSpeedDay_list = data[6]   # 风速
        windSpeedNight_list = data[10]
        print(windScaleDay_list)
        # print(len(windSpeedDay_list))
        # print(windScaleDay_list[i][windScaleDay_list[i].find('-')])
        # =========该注释块部分程序实现结果为：============================================
        # # 将 [xx, xx, xx, xx] 换行输出每个元素
        # for i in range(0, int(len(windSpeedDay_list))):
        #     ScaleDay_l = windScaleDay_list[i][:windScaleDay_list[i].find('-')]
        #     ScaleDay_r = windScaleDay_list[i][windScaleDay_list[i].find('-') + 1:]
        #     ScaleDay = [float(ScaleDay_l), float(ScaleDay_r)]
        #     windScaleDay_real = sum(ScaleDay) / 2
        #     print(windScaleDay_real)
        # =============================================================================
        # =========输出为列表 [xx, xx, xx, xx]==============
        windScaleDay_real_list = []
        for i in range(0, int(len(windScaleDay_list))):
            ScaleDay_l = windScaleDay_list[i][:windScaleDay_list[i].find('-')]
            ScaleDay_r = windScaleDay_list[i][windScaleDay_list[i].find('-') + 1:]
            ScaleDay = [float(ScaleDay_l), float(ScaleDay_r)]
            windScaleDay_real = sum(ScaleDay) / 2
            windScaleDay_real_list.append(windScaleDay_real)
        print(windScaleDay_real_list)  # 输出风级于一个列表中
        # =======（风级雷达图）数据可视化=========
        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(1, 1, 1, polar=True)  # 设置一个坐标轴为极坐标体系
        y = windScaleDay_real_list  # 风级
        label_list = []
        for i in range(0, 7):
            fxDate_list_simple = fxDate_list[i][2:]
            label_list.append(fxDate_list_simple)
        # print(label_list)
        label = np.array(label_list)  # 日期作为标签
        x = np.linspace(0, 2 * np.pi, len(y), endpoint=False)  # len(y)里有几个数据，就把整圆360°分成几份
        x1 = np.concatenate((x, [x[0]]))  # 将x的第一个值添加到原来的x组成第一个和最后一个元素一致的新列表，以实现x闭合
        y1 = np.concatenate((y, [y[0]]))  # 将y的第一个值添加到原来的y组成第一个和最后一个元素一致的新列表，以实现y闭合
        # 绘制极坐标
        angles = x
        ax.set_thetagrids(angles * 180 / np.pi, label, fontproperties="Microsoft YaHei")  # 设置网格标签(外环标签)
        ax.plot(x1, y1, "o-")
        ax.set_theta_zero_location('E')  # 设置极坐标0°位置
        ax.set_rlim(0, max(y))  # 设置显示的极径范围(内环值)
        ax.fill(x1, y1, facecolor='b', alpha=0.2)  # 填充颜色
        ax.set_rlabel_position(15)
        ax.set_title(str(city_ZH)+"未来7天风级变化", fontproperties="SimHei", fontsize=16)  # 设置标题
        plt.show()
# =========================绘制天气饼图===================================
        weather_list = data[11]
        weather_dict = {}
        for i in range(0, 7):
            if weather_list[i] in weather_dict.keys():
                weather_dict[weather_list[i]] += 1
            else:
                weather_dict[weather_list[i]] = 1
        # print(weather_dict)   # 天气状态 list -> dict
        explode = [0.01] * len(weather_dict.keys())
        color = ['lightskyblue', 'silver', 'yellow', 'salmon', 'grey', 'lime', 'gold', 'red', 'green', 'pink']
        plt.pie(weather_dict.values(), explode=explode, labels=weather_dict.keys(), autopct='%1.1f%%', colors=color)
        plt.title(str(city_ZH)+'未来7天气候分布饼图')
        plt.show()

# ================历史天气数据===（进行天气预测）===========================================
        # city_abc = 'fuling'
        from pypinyin import lazy_pinyin  # 汉子转拼音
        result = lazy_pinyin(city_ZH)  # 输出汉字的拼音列表
        # print(b)
        city_abc = ''.join(map(str, result))  # 输出汉字的拼音字符串
        # print(city_abc)

        historical_weather_url = 'http://www.tianqihoubao.com/weather/top/{}.html'.format(city_abc)
        print(historical_weather_url)
        html = requests.get(historical_weather_url).content.decode('gbk')  # content.decode('gbk')读取html网页内容并解码
        # print (html) #读取的内容是html的格式
        soup = BeautifulSoup(html, 'html.parser')  # 对html中无用的代码进行部分清理
        # print (soup)
        key_info_list = soup.find_all('tr')
        # print (key_info_list) # 寻找soup中所有和'tr'相关的字符串
        # print (key_info_list[2]) #找第三个元素
        # print(key_info_list[2:])  # 找第三个元素及其之后的元素
        # print (key_info_list[2].text) # 打印字符串列表中的文本
        # print(key_info_list[2].text.split())  # 默认空格与回车分离
        # print (key_info_list[2].text.split(sep='\n')) # split(sep='\n')可以指定分开方式

        dates, weather, temp, wind, wind_level, day_sign = [], [], [], [], [], []
        for data in key_info_list[2:]:
            # print (data.text)
            sub_data = (data.text.split())[1:]

            # dates
            dates.append((sub_data[0])[:10] + ' 11:00:00')  # (sub_data[0])[:10]表示dates数据列的前10个数据
            dates.append((sub_data[0])[:10] + ' 23:00:00')
            # weather
            weather.append(sub_data[1])
            weather.append(sub_data[5])
            # temp
            temp.append(sub_data[4][:-1])
            temp.append(sub_data[8][:-1])
            # wind
            wind.append(sub_data[2])
            wind.append(sub_data[6])
            # wind_level
            wind_level.append(sub_data[3])
            wind_level.append(sub_data[7])

            # day_sign
            day_sign.append(1)
            day_sign.append(0)
        # print(data.text.split())
        # print(sub_data)
        # print()
        # print(dates)
        # print(weather)
        # print(temp)
        # print(wind)
        # print(wind_level)
        # print(day_sign)

        history_data = pd.DataFrame({'date': pd.to_datetime(dates, format='%Y-%m-%d %H:%M:%S'),
                                     'day_sign': day_sign, 'weather': weather,
                                     'temp': np.array(temp, dtype=np.int64), 'wind': wind,
                                     'wind_level': wind_level})  # np.array(temp,dtype=np.int64)将temp规范成为整形变量
        # print(history_data)  # 得到历史数据表

        # ==========创建回归直线图============================================
        history_data = history_data.sort_values('date')  # 寻找数据表中 date列数据，并将数据表进行增序排序
        # 将白天时期的数据，即'day_sign==1'时，有多少天，作为横坐标
        X = (np.array(history_data.query('day_sign==1').date - history_data.query('day_sign==1')
                      .date.iloc[0]) / 1e9 / 86400).astype(int)
        X = X.reshape(-1, 1)[-5:]  # 取X的最后5位数，即最近5天
        y = np.array(history_data.query('day_sign==1').temp)[-5:]  # 纵坐标为最近5天的温度，temp
        # print(X)
        # print(y)
        linear_regr = linear_model.LinearRegression()  # 定义变量调用函数
        linear_regr.fit(X, y)  # 作拟合函数
        # print(linear_regr.coef_, linear_regr.intercept_)  # 斜率、截距
        # # ===========天气预测（3天）=============================
        X_new = np.concatenate((X, np.array([30, 31, 32]).reshape(-1, 1)))  # +预测温度未来3天的横坐标
        # print(X_new)
        y_new = linear_regr.predict(X_new)  # 预测温度的纵坐标

        plt.figure(figsize=(12, 9))
        plt.plot(X_new[-3:], y_new[-3:], 'bo', label='预测温度')
        plt.plot(X, y, 'ro', label='历史温度')
        plt.plot(X_new, y_new, 'g-')
        plt.title(str(city_ZH) + '未来3天温度预测图', fontsize=20)
        # plt.xlabel('未来天数/天')
        plt.ylabel('摄氏度/℃')
        plt.legend()
        plt.show()
# ================天气灾害预警  之  方法2：===========================================================
        # ====低温预警信号（2天内）：tempMin_list7天内最低温度(含今日)==============
        tempMin_2d = [tempMin_list[1], tempMin_list[2]]
        if min(tempMin_2d) in range(-5, -2):
            print("低温黄色预警：未来2天最低气温将至零下3℃")
        elif min(tempMin_2d) < -5:
            print("低温橙色预警：未来2天最低气温将至零下6℃")
        else:
            print()
