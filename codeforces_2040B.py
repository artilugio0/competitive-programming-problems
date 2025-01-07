for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue

    r = 4
    count = 2

    while r < n:
        r = 2*(r+1)
        count += 1

    print(count)
