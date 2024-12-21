xs = [[int(d) for d in input()] for _ in range(int(input()))]

def maximize(n, start):
    while start < len(n):

        for i in range(1, min(9, len(n) - start)):
            ni_i = n[start + i] - i

            if n[start] < ni_i:
                for j in range(i):
                    n[start+i-j], n[start+i-j-1] = n[start+i-j-1], n[start+i-j]

                n[start] = ni_i
                start -= 1
                break

        start += 1

    return n


for x in xs:
    print(''.join(str(i) for i in maximize(x, 0)))
