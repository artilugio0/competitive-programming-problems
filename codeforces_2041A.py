days = set(int(d) for d in  input().split())
for i in range(1, 6):
    if i not in days:
        print(i)
        break
