#!/usr/bin/env python
# coding:utf-8


""""
Name: 02_if_elif应用.py
Date: 2018/04/22
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 求平均成绩
#   1. 用户输入某个学生的姓名；
#   2. 输入该学生的语文， 数学与英语的成绩；
#   3. 打印:   姓名的成绩等级XXXX:



# avg_score
# 90~100   A
# 80~90    B
# 70~80     C
# 0~70     D
# other :   invaild score

"""

stuName = input("姓名:")
chinese = float(input("语文成绩:"))
math = float(input("数学成绩:"))
english = float(input("英语成绩:"))
avgScore = (chinese + math + english) / 3

# if avgScore>90 and avgScore<=100:
if 90 < avgScore <= 100:
    print("%s的等级为%s" % (stuName, 'A'))
elif 80<avgScore<=90:
    print("%s的等级为%s" % (stuName, 'B'))
elif 70<avgScore <=80:
    print("%s的等级为%s" % (stuName, 'C'))
elif 0<avgScore <=70:
    print("%s的等级为%s" % (stuName, 'D'))
else:
    print("%s的成绩是无效的" %(stuName))

