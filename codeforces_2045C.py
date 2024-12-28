s = input()
t = input()

dist = {}
for i in range(1, len(t)):
    c = t[-i-1] 
    if c not in dist:
        dist[c] = i

best = float('inf')
bestis = None
bestit = None
for i in range(1, len(s)):
    c = s[i]
    if c in dist and i+1 + dist[c] < best:
        best = i+1 + dist[c]
        bestis = i
        bestit = dist[c]

if bestis is None:
    print(-1)
else:
    print(s[:bestis] + t[-bestit- 1:])

