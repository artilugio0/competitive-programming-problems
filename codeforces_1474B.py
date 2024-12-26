import math

def is_prime(n):
    if 0 <= n <= 1:
        return False

    s = int(math.sqrt(n))
    for i in range(2, s+1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    d = int(input())
    a = 1

    f = d+1
    while not is_prime(f):
        f += 1
    a *= f

    f += d
    while not is_prime(f):
        f += 1
    a *= f

    print(a)
