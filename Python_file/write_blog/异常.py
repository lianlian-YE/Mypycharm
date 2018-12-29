def test1(n):                                   #定义函数test1
    n=int(n)
    if n==0:
        raise ValueError('invalid value %s'%n) #抛出一个valueerror异常
    return 10/n
def test2():
    try:
        test1(0)                                 #执行test1函数
    except Exception as e :                     #捕获异常
        print(e)                                #打印记录
        raise                                   #将异常抛出，可以定义其他函数处理异常，此处不做处理

# test1(0)
test2()