import math

def solve(k, l1, r1, l2, r2):
    count = 0
    for n in range(32+1):
        a = l1
        b = r1+1
        while a < b:
            mid = (a+b)//2
            if mid*(k**n) < l2:
                a = mid+1
            else:
                b = mid

        minx = a
        if minx > r1:
            continue


        a = l1
        b = r1+1
        while a < b:
            mid = (a+b)//2
            if mid*(k**n) <= r2:
                a = mid + 1
            else:
                b = mid

        maxx = a - 1
        if maxx < l1:
            break

        count += maxx - minx + 1

    return count


memo = {}
for _ in range(int(input())):
    inp = tuple(map(int, input().split()))
    if inp in memo:
        print(memo[inp])
        continue

    count = solve(*inp)
    memo[inp] = count

    print(count)
