def fun(n,a_n):
    if sum(a_n) % n != 0:
        print(-1)
    else:
        max_apple = max(a_n)
        min_apple = min(a_n)
        count = 0
        while max_apple - min_apple > 2:
            a_n[a_n.index(max_apple)] = max_apple - 2
            a_n[a_n.index(min_apple)] = min_apple + 2
            max_apple = max(a_n)
            min_apple = min(a_n)
            count += 1

        if a_n.count(a_n[0]) == n:
            print(count)
        else:
            print(-1)
if __name__=='__main__':
    n = int(input())
    a_n = [int(each) for each in input().split()]
    fun(n,a_n)