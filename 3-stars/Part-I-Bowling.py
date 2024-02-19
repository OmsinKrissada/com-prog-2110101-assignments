result = input().strip()
target = int(input())
total = 0
i = 0
for f in range(1, 11):
    if result[i : i + 3] == "XXX":
        sc = 30
    elif result[i : i + 2] == "XX":
        sc = 20 + int(result[i + 2])
    elif result[i] == "X" and result[i + 2] == "/":
        sc = 20
    elif result[i] == "X":
        sc = 10 + int(result[i + 1]) + int(result[i + 2])
    elif result[i + 1 : i + 3] == "/X":
        sc = 20
    elif result[i + 1] == "/":
        sc = 10 + int(result[i + 2])
    else:
        sc = int(result[i]) + int(result[i + 1])
    total += sc
    if result[i] == "X":
        i += 1
    else:
        i += 2
    if f == target:
        total = sc
        break
print(total)
