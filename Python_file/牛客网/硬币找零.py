'''
假设有几种硬币n，面值不同，如1、3、5，并且数量无限。请找出能够组成某个数目k的找零所使用最少的硬币数。
输入描述:
    首先输入整数T表示需要找零的面值
    然后输入整数n表示，可供选择的硬币的种数
    最后循环录入可供选择的硬币数组
输出描述:
    输出为一行，如果可以找零，输出所需的最小硬币数，否则输出-1
输入例子:
    63
    5
    1 2 5 21 25
输出例子:
    3
'''
def coin(k,n,li):
    """
    d(k)=min(d(k-li[i])+1)
    :param k:
    :param n:
    :param li:
    :return:
    """
    if k<min(li):
        return -1
    else:
        dp=[]
        dp.append(0)
        for i in range(k):
            for j in li:
                if j<=i:
                    dp.append(min(dp[i],dp[i-j]+1))
        return dp[k]
if __name__=='__main__':
    k=int(input())
    n=int(input())
    li=[int(i) for i in input().split()]
    print(coin(k,n,li))