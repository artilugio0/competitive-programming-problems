for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    total = 0
    zcount = 0
    prev = None
    for a in ai:
        if a == prev:
            continue

        total += 1
        if a == 0:
            zcount += 1

        prev = a


    if zcount == 0:
        print(1)
    elif zcount == total:
        print(0)
    elif zcount == 1 and (ai[0] == 0 or ai[-1] == 0):
            print(1)
    elif zcount == 2 and ai[0] == 0 and ai[-1] == 0:
            print(1)
    else:
        print(2)
