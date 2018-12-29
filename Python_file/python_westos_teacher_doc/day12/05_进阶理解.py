#!/usr/bin/env python
# coding:utf-8


""""
Name: 05_进阶理解.py
Date: 2018/05/27
Connect: xc_guofan@163.com
Author: lvah
Desc:


BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""

#
# try:
#     all_num = []
#     while True:
#         all_num.append(int(input("num:")))
# except KeyboardInterrupt:
#     pass
# print("输入综合为%s" %(sum(all_num)))
#


# try:
#     exit(0)
# except SystemExit as e:
#     print('程序结束!')
#     print(e)
#     print('hello')
#
#

#
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#






# import sys
#
# try:
#     f = open('/tmp/passwd')
#     s = f.readline()
#     i = int(s.strip())
#     print(a)
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
# else:
#     print('all ok')



import sys


# print(sys.argv)
# # 命令行后面跟的第一个参数;
# print(sys.argv[1])
# print(sys.argv[2])

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
    finally:
        f.close()