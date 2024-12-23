import math

def solve_quadratic():
    n, k = map(int, input().split())
    max_minutes = 4*60 - k

    # 5*i*(i+1)/2 <= max_minutes
    # i*(i+1) <= 2/5*max_minutes
    # i**2 + i <= 2/5*max_minutes
    # i**2 + i - 2/5*max_minutes <= 0
    # (-1 - sqrt(1 +8/5*max_minutes))/2 <= i <= (-1 + sqrt(1 +8/5*max_minutes))/2
    # 0 <= i <= (sqrt(1 +8/5*max_minutes) - 1)/2

    i = int((math.sqrt(1 + 8/5*max_minutes) - 1) / 2)
    print(min(i, n))


def solve_binary_search():
    n, k = map(int, input().split())
    max_minutes = 4*60 - k

    a = 1
    b = max_minutes

    while a < b:
        mid = a + (b - a)//2
        if 5*(mid*(mid+1))/2 <= max_minutes:
            a = mid + 1
        else:
            b = mid

    a -= 1
    print(min(a, n))


#solve_quadratic()
solve_binary_search()
