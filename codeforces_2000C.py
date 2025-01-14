for _ in range(int(input())):
    n = int(input())
    aa = [int(x) for x in input().split()]
    m = int(input())
    ss = [input() for _ in range(m)]

    for s in ss:
        if len(s) != len(aa):
            print('NO')
            continue

        seenletters = {}
        seennumbers = {}
        for a, c in zip(aa, s):
            if a not in seennumbers:
                seennumbers[a] = c

            if c not in seenletters:
                seenletters[c] = a

            if seenletters[c] != a or seennumbers[a] != c:
                print('NO')
                break
        else:
            print('YES')

