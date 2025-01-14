for _ in range(int(input())):
    n = int(input())
    aa = [int(x) for x in input().split()]
    bb = [int(x) for x in input().split()]

    if bb[0] != aa[0] and bb[0] != aa[-1]:
        print('Alice')
        continue

    if bb[0] == aa[0]:
        for a, b in zip(aa,bb):
            if a != b:
                print('Alice')
                break
        else:
            print('Bob')

        continue

    if bb[0] == aa[-1]:
        for i, b in enumerate(bb):
            a = aa[-i-1]
            if a != b:
                print('Alice')
                break
        else:
            print('Bob')

        continue
