for _ in range(int(input())):
    n = int(input())
    s = input()

    mid = set(c for c in s[1:-1] if c != '.')

    if s[0] == 'p' and ('s' in mid or s[-1] == 's'):
        print('NO')
        continue

    if s[-1] == 's' and ('p' in mid or s[0] == 'p'):
        print('NO')
        continue

    if len(mid) > 1:
        print('NO')
        continue

    print('YES')
