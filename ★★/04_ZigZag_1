lines = int(input())
r, b = [int(x) for x in input().split()]
min_red = max_red = r
min_blue = max_blue = b

is_even_line = True
for line in range(lines):
    raw = input()
    if raw == "Zig-Zag":
        print(f"{min_red} {max_blue}")
        break
    elif raw[0] == "Z":
        print(f"{min_blue} {max_red}")
        break
    else:
        r, b = [int(x) for x in raw.split()]
        if is_even_line:
            r, b = b, r
        min_red = min(min_red, r)
        max_red = max(max_red, r)
        min_blue = min(min_blue, b)
        max_blue = max(max_blue, b)
    is_even_line = not is_even_line
