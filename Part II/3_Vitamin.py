fruits = []

for i in range(int(input())):
    fields = input().split()
    fruits.append(fields)
    vit_count = len(fields)

command = input().split()
op = command[0]
if len(command) > 1:
    arg = command[1] if op == "get" else int(command[1])
if op != "show":
    fruits.sort()

if op == "show":
    for f in fruits:
        print(" ".join(f))
elif op == "max":
    filtered = [x[arg] for x in fruits]
    max_val = max(filtered)
    max_index = filtered.index(max_val)
    selected = fruits[max_index]
    print(selected[0], selected[arg])
elif op == "avg":
    total = 0
    for val in fruits:
        total += float(val[arg])
    print(round(total / len(fruits), 4))
elif op == "get":
    names = [x[0] for x in fruits]
    if arg in names:
        print(f'{arg} {" ".join(fruits[names.index(arg)][1:])}')
    else:
        print(f"{arg} not found")
elif op == "sort":
    transformed = [[x[arg], x[0]] for x in fruits]
    transformed.sort()
    print(" ".join([x[1] for x in transformed]))
