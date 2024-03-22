values = [int(x) for x in input().split()]
values.sort()

left = values[: len(values) // 2]
if len(values) % 2 == 0:
    right = values[len(values) // 2 :]
else:
    right = values[len(values) // 2 + 1 :]


def get_mid(l):
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]


Q1 = get_mid(left)
Q3 = get_mid(right)
IQR = Q3 - Q1
L = Q1 - 1.5 * IQR
U = Q3 + 1.5 * IQR

print(f"L = {L} U = {U}")

filtered = []
for n in values:
    if n < L or n > U:
        filtered.append(n)
if len(filtered) == 0:
    print("Not found")
else:
    print(" ".join([str(x) for x in filtered]))
