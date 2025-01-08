for _ in range(int(input())):
    n, k = map(int, input().split())
    aa = [int(a) for a in input().split()]

    aa.sort(key=lambda a: -a)

    sum = 0
    for a in aa:
        if sum + a > k:
            break
        sum += a

    if sum == k or sum == 0:
        print(0)
    elif sum < k:
        print(k-sum)
    else:
        raise Exception("unreachable")
