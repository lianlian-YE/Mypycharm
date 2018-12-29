class fruit(object):                  #定义一个类
    atest='this is a test'
    def __init__(self,name):          #定义属性name
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self.__name=name
        else:
            raise ValueError('name must be str')

f1=fruit('apple')                     #实例化一个对象，name=apple
f2=fruit(123)                          #实例化一个对象，name=123,原则上，我们希望name是一个字符串类型，可是，无法进行参数验证
# print(f1.name)                         #apple
# print(f2.name)                         #123
print(f1.name)
f1.name='banana'                   #可以直接对属性进行修改
print(f1.name)                         #banana
print(f1.atest)                         #banana
