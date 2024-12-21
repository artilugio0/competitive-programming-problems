import math

def solve(k, l1, r1, l2, r2):
    count = 0
    for n in range(32+1):
        if l1*(k**n) > r2:
            break

        if r1*(k**n) < l2:
            continue

        a = l1
        b = r1
        while a <= b:
            minx = (a+b)//2
            if minx*(k**n) < l2:
                a = minx+1
            else:
                b = minx-1

        if b < l1 or b*(k**n) < l2:
            minx = a
        else:
            minx = b

        a = l1
        b = r1
        while a <= b:
            maxx = (a+b)//2
            if maxx*(k**n) > r2:
                b = maxx-1
            else:
                a = maxx+1

        if a > r1 or a*(k**n) > r2:
            maxx = b
        else:
            maxx = a

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
