def taxi(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

count = int(input())
points = [([int(x) for x in input().split()]) for _ in range(count)]
limit = int(input())
traveled = 0

print(1, end='')
for i in range(0, len(points) - 1):
    distance = taxi(points[i], points[i + 1])
    traveled += distance
    if traveled <= limit:
        print(f' -> {i+2}[{traveled}]', end='')
    else:
        break
