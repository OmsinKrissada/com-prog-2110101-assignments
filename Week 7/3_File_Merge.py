merged = []
for fname in input().split():
    with open(fname) as f:
        for line in f.read().splitlines():
            merged.append([line[8:10], line])
merged.sort()
print("\n".join([x[1] for x in merged]))
