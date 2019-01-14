import cmath
def fun(h):
    '''
    x+x*x=h
    x*x+x-h=0
    a=1,b=1,c=-h
    :param h:
    :return:
    '''
    d=1+4*h
    # result1=(-1+cmath.sqrt(d))/2
    # result2=(-1-cmath.sqrt(d))/2
    result1=(-1+d**0.5)/2
    result2=(-1-d**0.5)/2
    result=result1 if result1>0 else result2
    return int(result)
if __name__=='__main__':
    h=int(input())
    print(fun(h))