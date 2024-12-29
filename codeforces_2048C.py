for _ in range(int(input())):
    s = input()

    first0 = None
    for i, c in enumerate(s):
        if c == '0':
            first0 = i
            break

    if first0 is None:
        print(1, len(s), 1, 1)
        continue

    best = 0
    idx = 0
    for i in range(0, first0):
        count = 0
        for j in range(len(s) - first0):
            if s[i+j] != s[first0+j]:
                count += 1
            else:
                break

        if count > best:
            idx = i
            best = count

    print(1, len(s), idx+1, idx+1+len(s)-first0-1)
