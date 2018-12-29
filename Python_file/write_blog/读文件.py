f=open('E:\\book\\test.txt','r')     #open函数打开一个文件，第一个参数文件名，第二个参数指打开方式，r表示只读
print(f.read())                        #read读取所有内容，并返回一个字符串
f.close()                              #关闭文件

try:
    f=open('E:\\book\\test.txt','r')
    print(f.read())
finally:                                #开始执行finally
    if f:                               #如果f还存在
        f.close()                       #关闭f对象

with open('E:\\book\\test.txt','r') as f:    #打开一个文件，并作为对象f
    print(f.read())                            #with语句结束，自动关闭对象
