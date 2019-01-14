#!encoding:utf-8
"""
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 50），表示地牢的长和宽。
接下来的 n 行，每行 m 个字符，描述地牢，地牢将至少包含两个 '.'。
接下来的一行，包含两个整数 x0, y0，
表示牛牛的出发位置（0 <= x0 < n, 0 <= y0 < m，左上角的坐标为 （0, 0），出发位置一定是 '.'）。
之后的一行包含一个整数 k（0 < k <= 50）表示牛牛合法的步长数，
接下来的 k 行，每行两个整数 dx, dy 表示每次可选择移动的行和列步长（-50 <= dx, dy <= 50）
"""
import queue
class point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def isOk(self):
        if  0<=self.x<n and 0<=self.y<m and  a[self.x][self.y]=='.':
            return True
        else:
            return False
    def go(self,d):
        return point(self.x+d[0],self.y+d[1])

if __name__=='__main__':
    n,m=[int(x) for x in input().split()]
    a=[]   #二维数组描述地牢
    use_point=0
    for i in range(n):
        a.append([x for x in input()])
        use_point+=a[i].count('.')
    x0,y0=[int(x) for x in input().split()]
    k=int(input())
    kli=[]  #存储步长
    for i in range(k):
        dx,dy=(int(x) for x in input().split())
        kli.append((dx,dy))
    print(n,m)
    print(a)
    print(x0,y0)
    print(k)
    print(kli)
    tt_li=[]
    start=point(x0,y0)
    q=queue.Queue()
    q.put(start)
    tt_li.append((start.x,start.y))
    eli=[[0 for j in range(m)]for i in range(n)]
    while not q.empty():
        temp=q.get()
        for i in kli:
            next_point=temp.go(i)
            ttemp=(next_point.x,next_point.y)
            if next_point.isOk and (ttemp not in tt_li):
                q.put(next_point)
                tt_li.append(ttemp)
                eli[next_point.x][next_point.y]=eli[temp.x][temp.y]+1
    if len(tt_li)==use_point:
        temppp=[]
        for x in eli:
            temppp.append(max(x))
        print(max(temppp))
    else:
        print(-1)

