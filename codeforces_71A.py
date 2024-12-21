n = int(input())
for _ in range(n):
    l = input()
    if len(l) <= 10:
        print(l)
        continue

    print(l[0] + str(len(l) - 2) + l[-1])
