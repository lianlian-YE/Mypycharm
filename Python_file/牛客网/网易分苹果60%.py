'''
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，
现在你要在它们之间转移苹果，使得最后所有奶牛拥有的苹果数都相同，
每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，
问最少需要移动多少次可以平分苹果，如果方案不存在输出 -1。
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数 n（1 <= n <= 100），
接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。
'''
def fun(n,ai):
    avg=sum(ai)//n
    li = ai
    result=0
    ma = max(li)
    mi = min(li)
    while ma!=mi:
        for x in range(0,n):
            for y in range(0,n):
                if li[x]<avg and li[y]>avg:
                    li[x]+=2
                    li[y]-=2
                    result+=1
                    ma=max(li)
                    mi=min(li)
        # if ma-mi<4 :
        #     result=-1
    for i in li:
        for j in li:
            if i!=j:
                return -1
            else:
                return result
    # return result
if __name__=='__main__':
    n=int(input())
    ai=[int(x) for x in input().split()[:n]]
    print(fun(n,ai))
