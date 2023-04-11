# -*- coding:utf-8 -*-
"""
作者：HET
主要完成相关类的定义
日期：2023年04月05日
"""
class Student(object):
    def __init__(self,id_,s_name):
        self.id_=id_
        self.s_name=s_name
        self.course=[]
    def course_detail(self):
        return self.course
    def add_course(self,cour_info):
        return self.course.append(cour_info)
        # return 'Name：{}，Selected：{}'.format(self.s_name,self.course)
    def str_s(self):
        return 'name:{},s_number:{}'.format(self.s_name,self.id_)

class Teacher(object):
    def __init__(self,t_id,t_name,phone):
        self.t_id=t_id
        self.t_name=t_name
        self.phone=phone
    def str_t(self):
        return self.t_id,self.t_name

class Course(object):
    def __init__(self,c_id,c_name):
        self.c_id=c_id
        self.c_name=c_name
        self.teacher=None
    def binding(self,teacher):
        if teacher:
           self.teacher = teacher
           return {'课程名称': self.c_name, '教师名称': self.teacher}
        else:
            return None




