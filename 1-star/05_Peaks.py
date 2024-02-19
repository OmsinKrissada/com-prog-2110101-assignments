n = [int(x) for x in input().split()]
count = 0
for i in range(1, len(n) - 1):
    if n[i - 1] < n[i] and n[i + 1] < n[i]:
        count += 1
print(count)
