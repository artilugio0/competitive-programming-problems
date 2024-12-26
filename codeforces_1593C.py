for _ in range(int(input())):
    n, k = map(int, input().split())
    xi = [int(x) for x in input().split()]
    xi.sort(key=lambda x: -x)

    cat = 0
    i = 0
    count = 0
    while i < len(xi):
        dist = n - xi[i]
        if cat < xi[i]:
            count += 1
            cat += dist
        else:
            break

        i += 1

    print(count)
