def fun3():
    f=[]
    def fun4(j):
        def fun5():
            return j ** 2  # 返回i的二次幂
        return fun5        #返回一个闭包，函数为j**2，运行环境为j
    for i in range(1,4):    #循环遍历1,2,3
       f.append(fun4(i))     #追加元素到f,每一个元素为一个闭包，在闭包内，变量恒为i
    return f

for i in fun3():
    print(i())
print(fun3,__name__)
