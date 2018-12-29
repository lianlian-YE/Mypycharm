#!/usr/bin/env python
#coding:utf-8


""""
Name: 20_学生管理系统_前期总复习.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 学生管理系统, 分为管理员登陆和学生登陆；

# 管理员登陆， 可以操作：
    # 管理员密码修改;
    # 添加学生的信息;
    # 删除学生的信息;
    # 修改学生的信息;
    # 查询学生的信息(根据学号);
    # 查看所有学生的信息;
    # 退出系统;



# 学生登录:
    # 查询个人信息;
    # 修改信息；
        # 修改年龄；
        # 修改密码;

# 学生信息包括:
    # 学号， 姓名， 性别， 班级， 出生年月， 用户名， 密码
    # 学生用户名和学号保持一致;


# 管理员信息包括:
#     用户名, 密码


# 学号作为key值
student_info = {
    '001': {


        'username':'001',
        'password': '001'

    }



}


admin_info = {
    "root":"passwd"
}


def student_menu():
    pass



def admin():
    pass





def main():
    while True:
        info = """"
                    学生管理系统
                    
            1). 以管理员
            2). student

        """
