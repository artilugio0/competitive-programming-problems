xs = [tuple(map(int, input().split())) for _ in range(int(input()))]

for (m,a,b,c) in xs:
    count = m if a > m else a
    count += m if b > m else b
    count = 2*m if c > 2*m - count else count + c
    print(count)

