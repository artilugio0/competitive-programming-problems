for _ in range(int(input())):
    s = input()
    best = 0
    j = 0
    for i in range(1, len(s) + 2):
        j += 1
        best = max(best, j)

        if i <= len(s) and s[-i] == 'R':
            j = 0

    print(best)
