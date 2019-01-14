def choir(n,a,k,d):
    dp=[(e,e) for e in a]  #初始值为二维数组，每个元素为(a[i],a[i])
    for i in range(1,k):
        dpp=dp[:i]    #取dp的前i个元素
        for j in range(i,n):
            temp_list=[]  #定义临时数组，用于接收a[j]与子序列的乘积
            for x in range(j-d,j):
                # print(x)
                if x<0:
                    continue
                else:
                    temp_list.append(a[j]*dp[x][0])
                    temp_list.append(a[j]*dp[x][1])
            dpp.append((max(temp_list),min(temp_list)))
        print(dp[:i])
        dp=dpp
        print(dp)
    return max([max(e) for e in dp])
if __name__=='__main__':
     n=int(input())
     a=[int(i) for i in input().split()]
     k,d=[int(i) for i in input().split()]
     print(choir(n,a,k,d))
