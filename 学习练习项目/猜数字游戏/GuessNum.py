# -*- coding:utf-8 -*-
"""
作者：HET
1、玩家根据提示进行数字区间起始位置和终止位置的输入
2、依据 1 中输入的数字区间，产生该区间内一个随机数，用于进行猜测比对的终值
3、提示用户输入所猜测的数字，与 2 中产生的随机数字进行比对，并将相应的信息写入指定的日志文件（日志文件名称：record.txt；日志文件路径：与.py文件处于同一级目录）
4、依据 3 中的比对结果。若两者不等，打印友好提示，重复 3、4 步骤；若两者相等，则退出该函数，执行下列语句
5、当猜测的值不在指定区间内时，不需要统计次数和记录
6、打印效果图，用以提示游戏结束的信息
日期：2023年04月02日
"""
import logging
import random
import sys
import time


# 游戏进入提示函数
def guide_page(guide_word):
    a = '*' * 15
    print(f'{a}{guide_word}{a}')


# 数字类型判断函数
def all_num(n):
    if n.isdigit():
        return True
    else:
        return False


# 数值合法性判定函数
def num_legal(ls):
    if ls[0] == ls[1]:
        print("您所输入的区间数字相同！！请重新启动程序")
        sys.exit()
    elif ls[0] > ls[1]:
        print("您所输入的数字区间大小有误！！请重新启动程序")
        sys.exit()
    else:
        return 1


# 产生指定区间随机数函数
def set_final_num(num1, num2):
    lst = [num1, num2]
    print(f"所产生的随机数字区间为：{lst}")
    result = list(filter(all_num, lst))
    if len(result) == 2:
        return True
    else:
        print("您所输入的为非数字字符串！！请重新启动程序")
        sys.exit()


# 核查数值是否属于指定区间函数
def check_num_legal(num):
    if int(i) <= num <= int(j):
        return 1
    else:
        return 0


# 日志写入函数
def write_record(times, value):
    format_ = '%(asctime)s%(filename)%s[line:%(lineno)d]%(levelname)s%(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=format_,
        filename='猜测日志.txt',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode='a')
    logging.info("第{}次您猜测的数字为：{}\n".format(times,value))



# 猜测数字并进行比对直到猜测到正确数字
def main(rand1):
    guess = int(input("请输入您猜测的数字："))
    count = 0
    while 1:
        if check_num_legal(guess) == 0:
            print("对不起您输入的数字未在指定区间！！！")
            guess = int(input("请重新输入："))
            # main(rand1)
            continue
        else:
            count += 1
            write_record(count, guess)
            if guess < rand1:
                print("您猜测的数字偏小")
                guess = int(input("请重新猜测一个数字："))
                write_record(count, guess)
                continue
            elif guess > rand1:
                print("您猜测的数字偏大")
                guess = int(input("请重新猜测一个数字："))
                write_record(count, guess)
                continue
            else:
                print("恭喜你！猜对了")
                break

if __name__ == '__main__':
    guide = '欢迎进入数字猜猜小游戏'
    guide_page(guide)
    i = input("请输入数字区间起始值：")
    j = input("请输入数字区间终止值：")
    set_final_num(i, j)
    temp = random.randint(int(i), int(j))
    main(temp)