for _ in range(int(input())):
    n = int(input())
    pi = [int(p)-1 for p in input().split()]

    count = 0
    visited = set()
    for i in range(len(pi)):
        if i in visited:
            continue
        c = pi[i]
        visited.add(c)
        length = 0
        while c != i:
            length += 1
            c = pi[c]
            visited.add(c)

        count += length//2

    print(count)
