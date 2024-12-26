n = int(input())
ai = [int(x) for x in input().split()]

ai.sort()

for i in range(n//2):
    ai[i*2], ai[i*2+1] = ai[i*2+1], ai[i*2]

if n % 2 == 0:
    print(n//2 - 1)
else:
    print(n//2)

print(' '.join(str(a) for a in ai))
