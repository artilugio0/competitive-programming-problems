for _ in range(int(input())):
    n, k = map(int, input().split())
    if k < n:
        k *= n // k
        if k < n:
            k += n

    a = k // n
    if k % n > 0:
        a += 1
    print(a)
