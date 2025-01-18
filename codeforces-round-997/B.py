import functools

for _ in range(int(input())):
    n = int(input())
    gg = [[x == '1' for x in input()] for _ in range(n)]

    def comp(a, b):
        if a == b:
            return 0
        if a < b:
            return -1 if gg[a-1][b-1] else 1

        return -1 if not gg[a-1][b-1] else 1

    l = list(x for x in range(1,n+1))
    l.sort(key=functools.cmp_to_key(comp))

    print(' '.join(str(x) for x in l))
