#!/usr/bin/env python
# coding:utf-8


""""
Name: 09_应用_图书管理系统.py
Date: 2018/05/19
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""


class Book(object):
    def __init__(self, name, author, state, bookIndex):
        self.name = name
        self.author = author
        # 0:借出 1：未借出
        self.state = state
        self.bookIndex = bookIndex

    # 打印对象时自动调用;str(对象)
    def __str__(self):
        return "书名:<%s> 状态:<%s>" % (self.name, self.state)


class BookManage(object):
    books = []

    def start(self):
        """图书管理初始化"""
        b1 = Book('python', 'Guido', 1, "INS888")
        self.books.append(b1)
        self.books.append(Book('java', 'hello', 1, "IGS888"))
        self.books.append(Book('c', 'westos', 1, "INS880"))

    def Menu(self):
        self.start()
        while True:
            print("""
                        图书管理系统
                    1. 查询
                    2. 增加
                    3. 借阅
                    4. 归还
                    5. 退出
             
             """)

            choice = input("Choice:")
            if choice == "1":
                pass
            elif choice == '2':
                self.addBook()
            elif choice == '3':
                self.borrowBook()
            else:
                print("清输入正确的选择!")

    def addBook(self):
        name = input("书名：")
        self.books.append(Book(name, input("作者:"), 1, input("书籍位置:")))
        print("添加图书%s成功!" % (name))

    def borrowBook(self):
        name = input("借阅书籍名称:")
        ret = self.checkBook(name)
        if ret != None:
            if ret.state == 0:
                print("书籍《%s》已经借出" % (name))
            else:
                ret.state = 0
                print("借阅%s成功" % (name))
        else:
            print("书籍《%s》不存在!" % (name))

    def checkBook(self, name):
        """查找书籍是否存在"""
        for book in self.books:
            # book: Book类创建的对象
            # book.name;
            if book.name == name:
                # 返回book对象
                return book
        else:
            return None

bookManage = BookManage()
bookManage.Menu()


