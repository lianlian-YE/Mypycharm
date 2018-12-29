import time
# def log(fun):                           #定义一个装饰器，接收函数fun为参数
#     def wrapper(*args,**kwargs):        #内部函数wrapper，定义具体的装饰操作
#         print('excute %s'%fun.__name__) #在函数执行前，打印excute 函数名
#         return fun(*args,**kwargs)      #执行函数
#     return wrapper
# @log                                   #用@为函数添加装饰器，相当于abc=log(abc)
# def abc():                            #abc=log(abc)，执行wrapper闭包，首先打印excute abc
#     time.sleep(1)                      #执行函数本身，等待一秒
#     print('my name is abc')           #执行打印方法
# def log(text):                          #定义一个装饰器，接收普通参数text
#     def decorator(fun):                #定义一个高阶函数，接收函数为参数
#         def wrapper(*args,**kwargs):        #内部函数wrapper，定义具体的装饰操作
#             print('%s %s'%(text,fun.__name__)) #在函数执行前，打印text 函数名
#             return fun(*args,**kwargs)      #执行函数
#         return wrapper                  #返回wrapper闭包
#     return decorator                    #返回decorator闭包
# @log('ready,go!')                      #用@为函数添加装饰器，并携带参数，相当于abc=log('ready go!')(abc)
# def abc():                            #abc=log('ready go!')(abc)，执行decorator闭包，再执行wrapper闭包，首先打印ready go! abc
#     time.sleep(1)                      #执行函数本身，等待一秒
#     print('my name is abc')           #执行打印方法
class log(object):
    def __init__(self,fun):                 #实例化需要接收一个函数
        self.fun=fun                         #将函数赋给类的fun属性，相当于接收一个函数作为参数
    def __call__(self, *args, **kwargs):    #能像方法一样被调用
        print('excute %s'%self.fun.__name__)#在函数执行前打印
        return self.fun()                   #执行函数
@log                                        #abc=log(abc)，将abc作为log类的一个实例
def abc():                                 #abc已经变成一个Log对象，调用__call__方法，先打印excute abc
    time.sleep(1)                           #睡眠
    print('my name is abc')                #打印my name is abc
if __name__=='__main__':
    abc()
