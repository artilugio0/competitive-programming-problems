k = int(input())
n = 1
i = 19
while n != k:
    i += 9
    s = 0
    x = i

    while x > 0:
        s += x % 10
        x //= 10
    if s == 10:
        n += 1

print(i)
