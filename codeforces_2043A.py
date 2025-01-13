
for _ in range(int(input())):
    n = int(input())

    count = 0
    while n > 3:
        n //= 4
        count += 1

    result = 2**count
    print(result)
