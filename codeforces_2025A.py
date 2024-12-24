for _ in range(int(input())):
    s = input()
    t = input()
    l = min(len(t), len(s))

    i = 0
    while i < len(s) and s[i] == t[i]:
        i += 1

    result = len(s) + len(t) - i + min(i, 1)

    print(result)
