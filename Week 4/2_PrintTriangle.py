size = int(input())

for line in range(size - 1):
    print('.' * ((2 * (size - line) - 1) // 2), end='')
    print('*', end='')
    print('.' * (2 * line - 1), end='')
    if line != 0:
        print('*', end='')

    print()
print('*' * (2 * size - 1))