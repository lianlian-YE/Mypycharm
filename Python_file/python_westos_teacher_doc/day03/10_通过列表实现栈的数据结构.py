#!/usr/bin/env python
#coding:utf-8


""""
Name: 10_通过列表实现栈的数据结构.py
Date: 2018/04/29
Connect: xc_guofan@163.com
Author: lvah
Desc:


a = 1

stack = [1,2,3,4]
# 栈的工作原理: 先进后出

# 入栈；
# 出栈:
# 栈顶元素:
# 栈长度
# 栈是否为空



# 2. 队列的工作原理： x先进先出
# 入队， 出队， 队头， 队尾， 队列长度， 队列是否为空, 显示队列元素

"""

stack = []



info = """
            栈操作
            
        # 1). 入栈； 
        # 2). 出栈:
        # 3). 栈顶元素
        # 4). 栈长度
        # 5). 栈是否为空     
"""

while True:
    print(info)

    choice = input("请输入选择:")

    if choice == '1':
        item = input("入栈元素:")
        stack.append(item)
        print("元素%s入栈成功" %(item))
    elif choice == '2':
        # 出栈先判断栈是否为空;
        if  not stack:
            print("栈为空， 不能出栈")
        else:
            # item是弹出的那个元素；
            item = stack.pop()
            print("元素%s出栈成功" %(item))
    elif choice == '3':
        if len(stack) == 0:
            print("栈为空， 无栈顶元素")
        else:
            print("栈顶元素为%s" %(stack[-1]))
    elif choice == '4':
        print("栈长度为%s" %(len(stack)))
    elif choice == '5':
        if len(stack) == 0:
            print("栈为空")
        else:
            print("栈不为空.")
    elif choice == 'q':
        print("欢迎下次使用!")
        break
    else:
        print("请输入正确的选择!")


