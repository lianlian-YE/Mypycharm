'''
竖切枚举+二分法
二分范围：0至所有田地价值和
可行性判断（关键）：假定二分值为mid。暴力枚举竖切的位置（三重循环），然后看横切能切多少刀。
枚举横切时，当这部分的4个矩形（新的一横与上面一横之间被竖着的边界以及竖切三刀形成的四个矩形）的价值都大于等于mid，
说明这一刀切得合理，从这个位置开始继续往下枚举横切。
如果最终横切的刀数大于等于4，那么说明这个值mid是合理的，否则不合理。
通过这样的不断压缩区间，最终必然能够得到答案。
'''
def fun(n,m,li):
    '''
    :param n:列数
    :param m: 行数
    :param li: 矩阵
    :return:
    '''
    temp=[]     #所有竖切的可能性
    for i in range(1,m-3):
        for j in range(i,m-2):
            for k in range(j,m-1):
                temp.append((i,j,k))
    lli=[]
    for x in li:
        lli=sum(x)
    mid=sum(lli)/2
    fmid=[]
    aa
    fag
    t = n // 2
    mmid = 0
    mid1 = 0
    for i in range(0, n):
        for j in range(0, t):
            mmid += li[i][j]
    for te in temp:
        for i in range(0, n):
            for j in range(t, m):
                mid1 += li[i][j]
        mmid=mmid if mmid<mid1 else mid1
if __name__=='__main__':
    n,m=(int(x) for x in input().split())
    li=[]
    for i in range(n):
        li.append([int(x) for x in input()])
