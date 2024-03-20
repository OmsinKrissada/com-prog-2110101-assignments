a, b = [input() for _ in range(2)]

if len(a) != len(b):
    print('Incomplete answer')
else:
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    print(count)