def solve_binary_search():
    for _ in range(int(input())):
        buckets = int(input())
        ss = sum(int(s) for s in input().split())

        a = 1
        b = ss
        while a < b:
            mid = (a+b)//2
            if mid*mid < ss:
                a = mid + 1
            else:
                b = mid

        if a*a == ss:
            print("YES")
        else:
            print("NO")

solve_binary_search()
