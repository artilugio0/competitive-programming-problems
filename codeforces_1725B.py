def solve_binary_search():
    n, d = map(int, input().split())
    pi = [int(p) for p in input().split()]

    pi.sort(key=lambda p: -p)

    def ok(w):
        if w > n:
            return False

        used = 0
        for i in range(w):
            pow = pi[i]
            used += d // pow + 1
            if used > n:
                return False
        return True

    lo = 0
    hi = n+1

    while lo+1 < hi:
        mid = (lo+hi)//2
        if ok(mid):
            lo = mid
        else:
            hi = mid

    print(lo)

def solve_greedy():
    n, d = map(int, input().split())
    pi = [int(p) for p in input().split()]

    pi.sort(key=lambda p: -p)

    wins = 0
    used = 0
    for i in range(n):
        pow = pi[i]
        used += d // pow + 1
        if used <= n:
            wins += 1
        else:
            break

    print(wins)


#solve_binary_search()
solve_greedy()
