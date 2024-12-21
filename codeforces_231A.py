n = int(input())
count = 0
for _ in range(n):
    count += int(sum(int(i) for i in input().split()) >= 2)
print(count)
