import os
os.getcwd()                     #查看当前所在路径
os.listdir('E:\\book')         #返回当前目录下的所有文件，以列表形式
os.path.abspath('E:\\book')    #返回路径的绝对路径
os.path.abspath('.')           #'.'表示当前路径
os.path.abspath('..')           #'..'表示当前路径的上一层
os.path.split('E:\\book')      #将路径分割成目录和文件的形式，返回元组('E:\\', 'book')
os.path.join('E:\\', 'book')   #路径拼接 E:\book
os.path.dirname('E:\\book')    #返回路径中的文件夹名称   E:\\
os.path.basename('E:\\book')   #返回路径中的文件名称    book
os.path.getatime('E:\\book')              #文件或文件夹最后访问时间戳
os.path.getctime('E:\\book')              #文件或文件夹创建时间戳
os.path.getmtime('E:\\book')              #文件或文件夹最后修改时间戳

os.path.getsize('E:\\book')    #返回文件或文件夹大小
os.path.exists('E:\\book')     #查看文件或文件夹是否存在
# print(os.path.join('E:\\', 'book'))
# print(os.path.split('E:\\book'))
# print(os.path.abspath('E:\\book'))
# print(os.path.abspath('.'))
# print(os.path.abspath('..'))
# print(os.path.abspath('..\\..\\'))