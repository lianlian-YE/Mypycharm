#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_字典_创建.py
Date: 2018/04/30
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""

# 定义空集合， 必须set(),
# {}默认的类型为字典;
d = {}
print(type(d))

# 字典: key-value值, 键值对；
# value值可以是任意数据类型: int,float,long, complex, list, tuple,set, dict
d = {
    '王旭': [18, '男', "请假"],
    '张龙': [18, '男', '俯卧撑']
}

print(d['张龙'])

d2 = {
    'a': 1,
    'b': 2
}

print(d2)

d3 = {
    'a': {1, 2, 3},
    'b': {2, 3, 4}
}
print(d3)



# 字典的嵌套;
students = {
    '13021001': {
        'name':'张龙',
        'age':18,
        'score':100
    },
    '13021003': {
        'name': '张',
        'age': 18,
        'score': 90
    }
}
print(students['13021003']['name'])



# 工厂函数;
l = list([1,2,3])
print(l)

d5 = dict(a=1, b=2)
print(d5)



#

cardinfo = {
    '001':'000000',
    '002':'000000'
}




# fromkeys第一个参数可以列表/tuple/str/set， 将列表的每一个元素作为字典的key值，
#  并且所有key的value值一致， 都为'000000';
print({}.fromkeys({'1', '2'}, '000000'))


# 字典必须是不可变数据类型;d = {[1,2,3]:1}(x)

# 可变数据类型:list, set,  dict
# 不可变: 数值类型， str, tuple

