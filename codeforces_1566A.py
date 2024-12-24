def solve_equation():
    for _ in range(int(input())):
        n, s = map(int, input().split())

        # x + x*(n//2) = s
        # x*(1 + n//2) = s
        # x = s/(1+n//2)
        result = s/(1+n//2)
        print(int(result))

def solve_binary_search():
    for _ in range(int(input())):
        n, s = map(int, input().split())

        # x + x*(n//2) = s
        a = 0
        b = 10**9+1
        while a < b:
            mid = (a+b)//2
            if mid + mid*(n//2) <= s:
                a = mid + 1
            else:
                b = mid

        print(a-1)

solve_binary_search()
