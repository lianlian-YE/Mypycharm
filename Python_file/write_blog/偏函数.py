# def int2(x,base=2):        #定义一个新函数，默认base=2
#     return int(x,base)     #返回函数，base有默认值
# print(int2('100'))
import functools

int2=functools.partial(int,base=2)