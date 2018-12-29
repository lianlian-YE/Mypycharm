class Student(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'my name is Student %s'%self.name
    def __str__(self):
        return 'this is a student object %s'%self.name
    def __iter__(self):
        return self
    def __getitem__(self, item):
        return 'a'
    def __setitem__(self, key, value):
        self.key=value
        return self
    def __delitem__(self, key):
        del self.key
        return self
    def __getattr__(self, item):
        if item=='score':
            return 99
    def __call__(self, *args, **kwargs):
        return '为%s疯狂打call'%self.name
s=Student('xiaoxinxin')              #实例化
s                        #返回结果：my name is Student xiaoxinxin
print(s)                 #返回结果：this is a student object xiaoxinxin
