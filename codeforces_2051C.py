for _ in range(int(input())):
    n, m, k = map(int, input().split())
    mm = [int(m) for m in input().split()]
    kk = [int(k) for k in input().split()]

    if n == k:
        print('1'*m)
        continue
    elif n - k >= 2:
        print('0'*m)
        continue

    unk = None
    for i in range(n):
        if i < len(kk) and kk[i] != i+1:
            unk = i+1
            break
    else:
        unk = n

    print(''.join('1' if m == unk else '0' for m in mm))
