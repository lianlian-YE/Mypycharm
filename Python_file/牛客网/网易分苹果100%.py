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
    if sum(ai)%n !=0:
        print(-1)
    else:
        li = ai
        ma = max(li)
        mi = min(li)
        result = 0
        while ma-mi > 2:
            li[li.index(ma)]=ma-2
            li[li.index(mi)]=mi+2
            ma=max(li)
            mi=min(li)
            result += 1
        # tt=li[0]
        if li.count(li[0])==n:
            # return result
            print(result)
        else:
            # return -1
            print(-1)
if __name__=='__main__':
    n=int(input())
    ai=[int(x) for x in input().split()]
    # print(fun(n,ai))
    fun(n,ai)