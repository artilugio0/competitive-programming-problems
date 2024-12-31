def my_solution():
    # O(n*log(n))
    minf = -10**9

    for _ in range(int(input())):
        n = int(input())
        r1 = (int(r) for r in input().split())
        r2 = (int(r) for r in input().split())
        m = list(zip(r1,r2))

        m.sort(key=lambda c: minf +c[1] if c[0] > c[1] else -c[0])

        cost = 0
        shifted = False
        for i, c in enumerate(m):
            if not shifted and c[0] > c[1] and i == len(m)-1:
                cost += c[0] + c[1]
                break

            if c[0] > c[1]:
                cost += c[0]
            elif shifted:
                cost += c[1]
            else:
                shifted = True
                if i > 0 and m[i-1][1] > c[0]:
                    cost += m[i-1][1] + c[1]
                else:
                    cost += c[0] + c[1]

        print(cost)

def editorial_solution():
    # O(n)
    for _ in range(int(input())):
        n = int(input())
        r1 = (int(r) for r in input().split())
        r2 = (int(r) for r in input().split())
        m = zip(r1,r2)

        cost = 0
        s1, s2, sm = -10**9, -10**9, -10**9
        for (r1, r2) in m:
            rm = max(r1, r2)
            cost += rm
            if r1+r2-rm > s1+s2-sm:
                s1 = r1
                s2 = r2
                sm = rm

        cost += s1+s2-sm
        print(cost)

editorial_solution()

