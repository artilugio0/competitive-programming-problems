def solve_binary_search():
    memo = {}

    for _ in range(int(input())):
        n, h = map(int, input().split())
        ai = input()

        key = (n, h, ai)
        if key in memo:
            print(memo[key])
            continue

        ai = ai.split()
        max1, max2 = 0, 0
        for a in ai:
            a = int(a)
            if a > max1:
                max1, max2 = a, max1
            elif a > max2:
                max2 = a

        # damage = 1*max1+ 0*max2
        # damage = 1*max1+ 1*max2
        # damage = 2*max1+ 1*max2
        # damage = 2*max1+ 2*max2
        # damage = 3*max1+ 2*max2
        # damage = 3*max1+ 3*max2
        # damage = max1*(i+1)//2 + max2*(i//2)

        lo = 1
        hi = h
        while lo < hi:
            mid = (lo+hi)//2
            damage = max1*((mid+1)//2) + max2*(mid//2)
            if damage < h:
                lo = mid + 1
            else:
                hi = mid

        memo[key] = lo
        print(lo)

solve_binary_search()
