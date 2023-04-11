# -*- coding:utf-8 -*-
"""
作者：HET
主要完成相应的业务逻辑，并进行如效果图
日期：2023年04月05日
"""
from example import Student, Teacher, Course    # 导入类模块

def introduction(str_title):
    print("{}{}{}".format('*'*10,str_title,'*'*10))
# 创建课程信息初始化
def prepare_course():
    course={
        "01": "网络爬虫", "02": "数据分析","03": "人工智能", "04": "机器学习",
        "05": "云计算", "06": "大数据","07": "图像识别", "08": "Web开发"
    }
    course_lst=[]
    for key,value in course.items():
        course_ins=Course(c_id=key,c_name=value)    # 实例化课程类
        course_lst.append(course_ins)
    # print(course_lst)
    return course_lst


# 创建教师信息初始化
def create_teacher():
    teacher=[
        ['T1', '张亮', '13301122001'],
        ['T2', '王朋', '13301122002'],
        ['T3', '李旭', '13301122003'],
        ['T4', '黄国发', '13301122004'],
        ['T5', '周勤', '13301122005'],
        ['T6', '谢富顺', '13301122006'],
        ['T7', '贾教师', '13301122007'],
        ['T8', '杨教师', '13301122008']
    ]
    teacher_lst=[]
    for i in range(len(teacher)):
        teach_ins=Teacher(t_id=teacher[i][0],t_name=teacher[i][1],phone=teacher[i][2])  # 实例化老师类
        teacher_lst.append(teach_ins)
    return teacher_lst

# 课程与教师逐一绑定
def course_to_teacher():
    lst=[]
    is_course=prepare_course()  # 实例化的课程列表
    is_teacher=create_teacher() # 实例化的教师列表
    # print(len(is_course))
    # print(len(is_teacher))
    step=0
    # course_instance是每个 课程类 的实例化对象

    teacher_name = []
    for i in range(len(is_course)):
        # course_1是每个 教师类 的实例化对象
        course_1=is_teacher[i]
        name = course_1.t_name
        teacher_name.append(name)
    # print(teacher_name)
    for course_instance in is_course:
        step -= 1
        cour_ins=course_instance.binding(teacher=teacher_name[step])    # 返回课程对应的老师
        # print(message_cour)
        lst.append(cour_ins)
    # print(lst)    # 详细课程与老师列表
    return lst

# 创建学生信息初始化
def create_student():
    is_student=['小亮', '小明', '李红', '小丽', 'Jone', '小彤', '小K', '慕慕']
    stu_id=list(range(1000,1008))
    stu_lst=[]
    for j in range(len(is_student)):
        stu_ins=Student(id_=stu_id[j],s_name=is_student[-j-1])  # 实例化学生类
        # print(stu_ins.str_s())
        stu_lst.append(stu_ins)
    return stu_lst


if __name__=='__main__':
    title1='慕课学院（1）班学生的信息'
    title2='慕课学院（1）班选课结果'
    introduction(title1)

    stu=create_student()
    for stu_instance in stu:
        print(stu_instance.str_s())

    introduction(title2)
    course=course_to_teacher()  # 课程列表
    select=[]
    x = 0
    for i in range(len(course)):
        stu_cour = Student.add_course(stu[i],course[i])
        ret=Student.course_detail(stu[i])
        select.append(ret)
        # print(set(ret))
    for stu_instance in stu:
        name = stu_instance.s_name
        print('Name：{}，Selected：{}'.format(name,select[x]))
        x+=1
