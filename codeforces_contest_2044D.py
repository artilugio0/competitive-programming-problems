for _ in range(int(input())):
    n = int(input())
    used = {}
    max_used = 1
    last_fill = -1

    for x in input().split():
        x = int(x)
        if x not in used:
            print(x, end=' ')
            used[x] = 1
        elif used[x] < max_used:
            print(x, end=' ')
            used[x] += 1
        else:
            for _ in range(n):
                last_fill = last_fill + 1 % n
                if last_fill+1 not in used:
                    print(last_fill+1, end=' ')
                    used[last_fill+1] = 1
                    break
                elif used[last_fill+1] < max_used:
                    print(last_fill+1, end=' ')
                    used[last_fill+1] += 1
                    break
            else:
                print(x, end=' ')
                used[x] += 1
                max_used += 1

    print("")
