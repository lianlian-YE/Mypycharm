#!/usr/bin/env python
# coding:utf-8


""""
Name: 10_os模块应用_文件后缀名修改.py
Date: 2018/05/13
Connect: xc_guofan@163.com
Author: lvah
Desc:


# 题目:
# 创建文件/mnt/hello{1..8}.jpg   /mnt/westos{a..d}.py
# 修改所有的.jpg结尾的文件为/mnt/hello{1..8}.png;

"""

import os


def create_files(dirname):
    # hello{1..8}.jpg
    jpg_files = ['hello' + str(i) + '.jpg' for i in range(8)]
    # westos{a..d}.py
    py_files = ['westos' + str(i) + '.py' for i in ['a', 'b', 'c', 'd']]

    for file in jpg_files + py_files:
        filename = dirname + file
        if not os.path.exists(filename):
            os.mknod(filename)
            print("%s文件创建成功!" % (filename))
        else:
            print("%s文件已经存在!" % (filename))


def modify_suffix(dirname, old_suffix, new_suffix):
    if '.' not in old_suffix:
        old_suffix = "." + old_suffix

    if '.' not in new_suffix:
        new_suffix = '.' + new_suffix

    # 1. 判断目录是否存在
    if os.path.exists(dirname):
        # 2. 找出所有以.jpg结尾的文件;  # hello1.jpg   ====> hello1.png
        jpgnames = [filename for filename in os.listdir(dirname) if filename.endswith(old_suffix)]
        # 3. 所有以.jpg结尾的文件，去掉后缀名
        base_names = [os.path.splitext(filename)[0] for filename in jpgnames]
        for filename in base_names:
            dirname = os.path.abspath(dirname) + os.path.sep
            old_name = dirname + filename + old_suffix
            new_name = dirname + filename + new_suffix
            # 重命名时一定要用绝对路径;
            os.rename(old_name, new_name)
            print("%s重命名为%s成功!" % (old_name, new_name))
    else:
        print("%s目录不存在" % (dirname))
modify_suffix('/mnt', '.c', '.py')

#
# def modify_suffix(dirname, old_suffix, new_suffix):
#     """
#     修改指定目录下文件的后缀名
#     """
#     # if '.' not in old_suffix:
#     #     old_suffix = '.' + old_suffix
#     # if '.' not in new_suffix:
#     #     new_suffix = '.' + new_suffix
#
#     if os.path.exists(dirname):
#         all_jpg_files = [os.path.splitext(file)[0] for file in os.listdir(dirname)
#                          if file.endswith(old_suffix)]
#         for file in all_jpg_files:
#             basename = os.path.abspath(dirname) + os.path.sep
#             oldname = basename + file + old_suffix
#             newname = basename + file + new_suffix
#             os.rename(oldname, newname)
#             print("重命名%s为%s成功!" % (oldname, newname))
#     else:
#         print("%s目录不存在!" % (dirname))
#
#
# modify_suffix('/mnt', 'png', '.jpg')


# create_files()
