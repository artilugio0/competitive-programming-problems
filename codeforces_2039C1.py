for _ in range(int(input())):
    x, m = map(int, input().split())

    count = 0
    for y in range(1, min(2*x, m+1)):
        if y == x:
            continue
        xor = x^y
        if (x//xor)*xor == x or (y//xor)*xor == y:
            count += 1

    print(count)
