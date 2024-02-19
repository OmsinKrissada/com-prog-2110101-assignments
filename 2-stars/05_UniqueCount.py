l = [int(x) for x in input().split()]
l.sort()
unique = [l.pop(0)]

for n in l:
    if n > unique[-1]:
        unique.append(n)

print(len(unique))
print(unique[:10])
