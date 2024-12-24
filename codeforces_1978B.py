def solve_binary_search():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())

        # b, b-1, b-2, ..., b-(k-1) = k*b - (k-1)*k//2
        # p = k*b - (k-1)*k//2 + (n-k)*a
        l = 0
        h = min(n, b)

        while l < h:
            mid = (l+h)//2
            profit = mid*b - mid*(mid-1)//2 + (n-mid)*a
            profit_next = (mid+1)*b - (mid+1)*(mid)//2 + (n-mid-1)*a

            if profit < profit_next:
                l = mid + 1
            else:
                h = mid

        profit = l*b - l*(l-1)//2 + (n-l)*a
        print(profit)

solve_quadratic()
