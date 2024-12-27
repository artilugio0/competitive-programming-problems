import math

def solve_quadratic():
    n, k = map(int, input().split())

    s = int(math.sqrt(9+8*n+8*k))
    c1 = (3 + 2*n + s)//2
    c2 = (3 + 2*n - s)//2

    if c1 <= n:
        print(c1)
    else:
        print(c2)

def solve_binary_search():
    n, k = map(int, input().split())
    def ok(c):
        return ((n-c)*(n-c+1))//2 - c >= k

    lo = 0
    hi = n

    while lo+1 < hi:
        mid = (lo+hi)//2
        if ok(mid):
            lo = mid
        else:
            hi = mid

    print(lo)

solve_binary_search()
