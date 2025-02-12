op = input()


if op == "str2RLE":
    data = input()
    prev = data[0]
    count = 0
    for c in data:
        if prev == c:
            count += 1
        else:
            print(prev, count, end=" ")
            count = 1
            prev = c
    print(prev, count, end=" ")
elif op == "RLE2str":
    data = input()
    is_character = True
    for e in data.split():
        if is_character:
            character = e
        else:
            print(character * int(e), end="")
        is_character = not is_character
else:
    print("Error")
