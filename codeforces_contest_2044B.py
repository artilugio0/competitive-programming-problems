ss = [list(input()) for _ in range(int(input()))]
for s in ss:
    inv = []
    for c in s[::-1]:
        if c == 'p':
            inv.append('q')
        elif c == 'q':
            inv.append('p')
        else:
            inv.append('w')

    print(''.join(inv))
