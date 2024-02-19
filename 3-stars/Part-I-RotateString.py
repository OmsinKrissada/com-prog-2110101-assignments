op = input()
rows = int(input())
cols = 0
data = ""
is_invalid = False
for _ in range(rows):
    received = input().strip()
    data += received
    if len(received) != cols and cols != 0:
        is_invalid = True
        break
    cols = len(received)

if is_invalid:
    print("Invalid size")
elif op == "90":
    for i in range(cols):
        for j in range(rows):
            print(data[(rows - j - 1) * cols + i], end="")
        print()
elif op == "180":
    for i in range(rows):
        for j in range(cols):
            print(data[(rows - i - 1) * cols + (cols - j - 1)], end="")
        print()
elif op == "flip":
    for i in range(rows):
        for j in range(cols):
            print(data[((cols) * (i + 1) - 1) - j], end="")
        print()
