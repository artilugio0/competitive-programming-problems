import math

def solution1():
    n = int(input())
    count = 0

    # 25, 25    rem: 10
    count += n//2

    # 21, 21, 18    rem: 0
    count += n//2

    # at this point either we have all 25 and 21 or 1 of each are missing
    # if 1 of each are missing, we add 1: 25, 21, rem: 4
    count += n%2

    # at this point we have n//2 18, so math.ceil(n/2) are missing
    # 18, 18, 18, rem: 6
    count += math.ceil(math.ceil(n/2)/3)

    print(count)

solution1()
