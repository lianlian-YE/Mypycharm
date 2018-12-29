# class test(object):                 #class关键字用于定义类，（object）是指，进程于object类
#     def __init__(self,name,result): #__init__是构造函数，可以理解为，实例化变量时默认执行的函数，第一个参数必须是selt
#         self.name=name               #name和result分别为test的属性，在实例化的时候需要传入
#         self.result=result
#     def testfun(self):              #第一个参数必须为self，可以接收各种参数，默认参数，关键字参数，可变参数等。
#         return self.result.upper()  #可以通过self对对象属性进行操作。
#
# t1=test('a','ok')                   #实例化对象，name=a,result=ok
# def fun():
#     return (t1.result.upper())
# print(fun())
# print(t1.name)
# print(t1.result)
# print(t1.testfun())
class Transportation(object):
    def run(self):
        return 'Transportation is running'
class car(Transportation):
    def run(self):
        return 'car is running'
class bus(Transportation):
    def run(self):
        return 'bus is running'
t=Transportation()
c=car()
b=bus()
def test(Transportation):
    return Transportation.run()
print(test(t))
print(test(c))
print(test(b))