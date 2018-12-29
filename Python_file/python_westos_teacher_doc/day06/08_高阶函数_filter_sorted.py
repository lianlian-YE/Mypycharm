#!/usr/bin/env python
#coding:utf-8


""""
Name: 08_高阶函数_filter_sorted.py
Date: 2018/05/06
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


# filter高阶函数: filter(func, iterable)
#   1. func: 只有一个形参， 函数的返回值只能是True或者False；


def isodd(num):
    if num %2 == 0:
        return True
    else:
        return False
print(list(filter(isodd, range(10))))



def isPrime(num):
    pass
print(list(filter(isPrime, range(1000))))




# sorted:
# 排序： 由大到小
print(sorted([23,56546,78]))

# 排序： 由小到大， reverse=True, 代表排序后进行反转;
print(sorted([23,56546,78], reverse=True))




info = [
    ['001', 'apple', 1000, 2],
    ['002', 'xiaomi', 10, 2000],
    ['003', 'Oppo', 200, 1900],
    ['004', 'computer', 900, 5000]
]

def sorted_by_count(item):
    return item[2]

print(sorted(info, key=sorted_by_count))

# 需要按照商品的价格进行排序, 最终显示价格最高的商品名称和商品数量;

def sorted_by_price(item):
    return item[-1]
sorted_by_price_info = sorted(info, key=sorted_by_price)
print(sorted_by_price_info[-1][1], sorted_by_price_info[-1][2])







info = {
    '001':{
        'name':'apple',
        'count':1000,
        'price':2
    },

    '002': {
        'name': 'xiaomi',
        'count': 10,
        'price': 2000
    },
    '003': {
        'name': 'Oppo',
        'count': 200,
        'price': 1900
    }
}


def dict_sorted_by_count(item):
    return item['count']
print(sorted(info.values(), key=dict_sorted_by_count))