# -*- coding:utf-8 -*-
"""
作者：HET
类函数的使用
日期：2023年03月28日
"""

class Cat(object):
    # 创建构造函数
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def show_info(self):
        """ 显示猫的信息 """
        print(f'我叫{self.name}，今年{self.age}。我是{self.color}的')
    def eat(self):
        """ 吃 """
        print('我喜欢吃鱼')
    def catch(self):
        """ 猫捉老鼠 """
        print('我能捉老鼠')
# 创建两只猫的实例对象，并调用相应的方法
test1 = Cat("花花", 2, "黑色")
test1.show_info()
test1.catch()
test2 = Cat("雪球", 3.5, "白色")
test2.show_info()
test2.catch()
