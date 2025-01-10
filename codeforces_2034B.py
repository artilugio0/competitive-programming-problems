for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()

    i = 0
    onecount = 0
    result = 0
    while i < len(s):
        if s[i] == '0':
            onecount += 1
        elif s[i] == '1':
            onecount = 0

        if onecount == m:
            result += 1
            onecount = 0
            i += k-1

        i += 1

    print(result)

