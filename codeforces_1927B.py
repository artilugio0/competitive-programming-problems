for _ in range(int(input())):
    n = int(input())
    aa = [int(x) for x in input().split()]

    freqs = {
        0: set('abcdefghijklmnopqrstuvwxyz'),
    }

    s = []
    for a in aa:
        c = freqs[a].pop()
        s.append(c)
        f = freqs.get(a+1, set()) 
        f.add(c)
        freqs[a+1] = f

    print(''.join(s))
