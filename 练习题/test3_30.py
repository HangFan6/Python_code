# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年03月30日
"""

# =============super超类================================
# class Person(object):
#     # 重写实例对象的构造（初始化）方法
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     # 自定义实例方法，格式化打印实例属性name的值
#     def speak(self):
#         print(f'hello!我是{self.name}')
#
#     # 自定义实例方法，占位作用
#     def relation(self):
#         pass
#
#
# class Student(Person):
#     __stu_num = '2018014002'
#
#     # 重写实例对象的构造（初始化）方法，并调用父类构造方法，实现对实例属性的赋值
#     def __init__(self,name,gender, score, major):
#         self.score = score
#         self.major = major
#         super(Student, self).__init__(name, gender)
#
#     # 自定义实例方法，格式化打印实例属性stu_num的值
#     def speak(self):
#         # print(f'hello!我是{self.name}')
#         super(Student, self).speak()
#         print(f'我的学号为{self.__stu_num}，很高兴认识大家')
#
#     # 自定义实例方法，判断学号是否为既定值，并根据判断结构 进行分类打印
#     def identify_stu(self):
#         if self.__stu_num == '2018014002':
#             print("我的分组已经完成")
#         else:
#             print("请稍后，马上为你自动分组")
#
#     # 自定义实例方法，设置实例对象的学号为传入的值
#     def set_num(self, new_num):
#         self.__stu_num = new_num
#
#     # 自定义实例方法，判断该类是否为Person类的子类，并进行分类打印
#     def relation(self):
#         if issubclass(Student, Person):
#             print("我的父类是Person")
#         else:
#             print("父类正在查询中······")
#
#
# if __name__ == '__main__':
#     stu = Student('小明', '男', 90, '数学')
#     # 调用speak方法 打印stu对应的值
#     stu.speak()
#     # 调用实例方法 鉴别学号是否为指定值
#     stu.identify_stu()
#     # 调用实例方法 鉴别实例对象所属的类的父类是否为Person
#     stu.relation()
#     print("******************")
#     stu_2 = Student('小红', '女', 89, '英语')
#     # 调用实例方法 设置stu_2的学号为'2018040625'
#     stu_2.set_num('2018040625')
#     # 调用实例方法 打印stu_2对应的值
#     stu_2.speak()
#     # 调用实例方法 鉴别学号是否为指定值
#     stu_2.identify_stu()


# class Point(object):
#     # 自定义Point类的构造(初始化)方法
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # 自定义Point类对象的格式化输出函数(string())
#     def string(self):
#         print("{X：%d，Y：%d}" % (self.x, self.y))
#
#
# class Circle(Point):
#     # 自定义Circle类的构造(初始化)方法
#     def __init__(self, x, y, radius):
#         Point.__init__(self,x, y)
#         self.radius = radius
#     # 自定义Circle类对象的格式化输出函数(string())
#     def string(self):
#         print("该图形初始化点为：{X：%d, Y：%d}; {半径为：%d}"%(self.x,self.y,self.radius))
#
# class Size(object):
#
#
#     # 自定义Size类的构造(初始化)方法
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     # 自定义Size类对象的格式化输出函数(string())
#     def string(self):
#         print("{Width：%d, Height：%d}"%(self.width,self.height))
# class Rectangle(Point, Size):
#     # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
#     def __init__(self,x,y,width,height):
#         Point.__init__(self,x,y)
#         Size.__init__(self,width,height)
#
#     # 自定义Rectangle类对象的格式化输出函数(string())
#     def string(self):
#         print("该图形初始化点为：{X：%d, Y：%d}; 长宽分别为：{Width：%d, Height：%d}"%(self.x,self.y,self.width,self.height))
# if __name__ == "__main__":
#     # 实例化Circle对象，圆心为（5,5），半径为8
#     c=Circle(5,5,8)
#     c.string()
#     # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
#     r1=Rectangle(15,15,15,15)
#     r1.string()
#     # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
#     r2=Rectangle(40,30,11,14)
#     r2.string()


# # ==========双色球开奖==============
# import random
# num=[]
# # 摇出6个红色球号码和1个蓝色球号码
# for r in range(0,6):
#     red = random.randint(1, 33)
#     if red < 10:
#         red = '0' + str(red)
#     num.append(red)
# blue=random.randint(1,16)
# if blue<10:
#     blue='0'+str(blue)
# num.append(blue)
# print(f"本期双色球中奖号码：\n {num[0]} {num[1]} {num[2]} {num[3]} {num[4]} {num[5]} {num[6]}")


# ===========进程池===================
# import time
# import json
# import multiprocessing
#
#
# class Work(object):
#     def __init__(self, q):
#         self.q=q
#     def send(self,message):
#         if not isinstance(message,str):
#             message=json.dumps(message)
#         self.q.put(message)
#     def send_all(self):
#         for i in range(20):
#             self.q.put(i)
#             time.sleep(1)
#     def receive(self):
#         while 1:
#             result=self.q.get()
#             try:
#                 res=json.loads(result)
#             except:
#                 res=result
#             print('resc is %s'% res)
# if __name__=='__main__':
#     q=multiprocessing.Queue()
#     work=Work(q)
#     send=multiprocessing.Process(target=work.send,args=({'name':'小慕'},))
#     recv=multiprocessing.Process(target=work.receive)
#     send_all_p=multiprocessing.Process(target=work.send_all)
#
#     send_all_p.start()
#     send.start()
#     recv.start()
#
#     send_all_p.join()   # 阻塞最长使用率的进程
#     recv.terminate()    # 终结接收端

# ============线程==================
# import random
# import time
# import threading
#
# lst=['python','django','tornado','flask','bs5','requests','uvloop']
# new_lst=[]
# def work():
#     if len(lst)==0:
#         return
#     data=random.choice(lst)
#     lst.remove(data)
#     new_data='%s_new'%data
#     new_lst.append(new_data)
#     time.sleep(1)
#
# if __name__=='__main__':
#     start=time.time()
#     print('old list len:', len(lst))
#     t_lst=[]
#     for i in range(len(lst)):
#         t=threading.Thread(target=work)
#         t_lst.append(t)
#         t.start()
#     for t in t_lst:
#         t.join()
#     print('old list:',lst)
#     print('new list:',new_lst)
#     print('new_list len:',len(new_lst))
#     print('time is %s'%(time.time()-start))


# ===============线程池=====================
# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
# # 线程锁使用
# lock=threading.Lock()
# def work(i):
#     lock.acquire()
#     print(i)
#     time.sleep(1)
#     lock.release()
#
# if __name__=='__main__':
#     t=ThreadPoolExecutor(2)   # 设置2个线程
#     for i in range(20):
#         t.submit(work,(i,))


# # =========异步==================
# import os
# import asyncio
# import time
# import random
#
# async def a():
#     for i in range(10):
#         print(i,'a',os.getpid())
#         await asyncio.sleep(random.random() * 2)
#     return 'a function'
# async def b():
#     for i in range(10):
#         print(i,'b',os.getpid())
#         await asyncio.sleep(random.random()*2)
#     return 'b function'
# async def main():
#     result=await asyncio.gather(a(),b())
#     print(result)
#
# if __name__=='__main__':
#     start=time.time()
#     asyncio.run(main())
#     print(time.time()-start)
#     print('parent is %s'% os.getpid())

# import os
# import asyncio
# import time
# import random
# import gevent
#
# def gevent_a():
#     for i in range(10):
#         print(i,'a gevent',os.getpid())
#         gevent.sleep(random.random() * 2)
#     return 'gevent a result'
# def gevent_b():
#     for i in range(10):
#         print(i,'b gevent',os.getpid())
#         gevent.sleep(random.random() * 2)
#     return 'gevent b result'
#
# async def a():
#     for i in range(10):
#         print(i,'a',os.getpid())
#         await asyncio.sleep(random.random() * 2)
#     return 'a function'
# async def b():
#     for i in range(10):
#         print(i,'b',os.getpid())
#         await asyncio.sleep(random.random()*2)
#     return 'b function'
# async def main():
#     result=await asyncio.gather(a(),b())
#     print(result)
#
# if __name__=='__main__':
#     start=time.time()
#     g_a=gevent.spawn(gevent_a)
#     g_b=gevent.spawn(gevent_b)
#     gevent_list=[g_a,g_b]
#     result=gevent.joinall(gevent_list)
#     print(result)
#
#     print(time.time()-start)
#     print('parent is %s'% os.getpid())


# ================正则表达式===========
import re

# data='dewei@headwork.com'
# result=re.findall('\w{4,6}',data)
# print(result)

# test='hello my name is dewei'
# result=re.search('hello (.*) name is (.*)',test)
# print(result.groups())
# print(result.group(1))
# print(result.group(2))

# str_1 = 'I don\'t want to be your entire world, just the best thing in it, I want to say "$%^&*@#~!".'
# str_2 = "12i3 love 34you3 not 56because of 7who3 119  df44"
# print(re.findall('["].*["]',str_1))
# print(re.findall('"(.*)"',str_1))
#
# print(re.findall('\d\w+\d',str_2))
# print(re.findall('\d\w*\d',str_2))

# def get_email(data):
#     # result=re.findall('[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]+',data)
#     result=re.findall('.+@.+\.[a-zA-Z]+',data)
#     return result
# if __name__=='__main__':
#     email='dewei@imooc.com'
#     print(get_email(email))

# html=('<div class="s-top-nav" style="display:none;">'
#      '</div><div class="s-center-box"></div>')
# def get_html_data(data):
#     result=re.findall('style="(.*?)"',data)
#     return result
# def get_all_html(data):
#     result=re.findall('="(.+?)"',data)
#     return result
# if __name__=='__main__':
#     result=get_html_data(html)
#     print(result)
#     result=get_all_html(html)
#     print(result)

# email=['lianflower@163.com','11123433@qq.com','xinlang@sina.com']
# def get_email(data):
#     result=re.findall('@(.*)\.',data)
#     return result
# if __name__=='__main__':
#     for i in range(len(email)):
#         result=get_email(email[i])
#         print(result)
#         if result=='163':
#             print('163邮箱')
#         elif result=='qq':
#             print('qq邮箱')
#         else:
#             print('新浪邮箱')

# noodles='康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅'
# def check(data):
#     result=re.findall('康[^师]傅',noodles)
#     return result
# if __name__=='__main__':
#     result=check(noodles)
#     print("小慕买了%d包山寨商品"%len(result))

def memory(data,l=[]):
    l.append(data)
    print(l)
memory('I')
memory('love',[])
memory('imooc')


