from collections import defaultdict

for _ in range(int(input())):
    n,x = map(int, input().split())
    ai = [int(a) for a in input().split()]

    freq = defaultdict(int)
    for a in ai:
        freq[a] += 1

    for k in range(len(ai)):
        if freq[k] == 0:
            print(k)
            break

        if freq[k] > 1:
            freq[k+x] += freq[k]-1
            freq[k] = 1
    else:
        print(len(ai))


