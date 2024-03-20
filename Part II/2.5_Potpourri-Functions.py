def convex_polygon_area(p):
    total = 0
    for i in range(len(p)):
        total += p[i][0] * p[(i + 1) % len(p)][1]
    for i in range(len(p)):
        total -= p[i][1] * p[(i + 1) % len(p)][0]
    return abs(total / 2)


def is_heterogram(s: str):
    found = []
    for c in s:
        if not c.isalpha():
            continue
        tc = c.lower()
        if tc in found:
            return False
        found.append(tc)
    return True


def replace_ignorecase(s, a, b):
    transformed = list(s)
    i = 0
    while i < len(s):
        if s[i:i+len(a)].lower() == a.lower():
            transformed[i:i+len(a)] = list(b)
            i += len(a)
        i += 1
    return ''.join(transformed)


def top3(v):
    converted = sorted(list(v.items()))
    num_sorted = sorted([(v, k) for k, v in v.items()])
    num_sorted.reverse()
    highest_nums = [x[0] for x in num_sorted]
    out = []
    for n in highest_nums:
        for i, lookup in enumerate(converted):
            if lookup[1] == n:
                out.append(lookup[0])
                converted.pop(i)
                break

    return out[:3]


for k in range(2):
    exec(input().strip())
