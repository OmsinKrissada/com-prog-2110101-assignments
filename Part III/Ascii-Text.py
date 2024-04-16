# with open("ignore/ascii_data.txt") as f:
with open(input().strip()) as f:
    lines = [l.strip() for l in f.readlines()]

gaps = []
for col in range(len(lines[0])):
    found_letter_part = False
    for row in range(len(lines)):
        if lines[row][col] != ".":
            found_letter_part = True
            break
    if not found_letter_part:
        gaps.append(col)


def remove(lines, remove_arr):
    result = []
    for line in lines:
        line_buffer = ""
        for idx in range(len(line)):
            if idx in remove_arr:
                continue
            line_buffer += line[idx]
        result.append(line_buffer)
    return result


def lstrip(g):
    removing = []
    for i in range(len(g)):
        if i != g[i]:
            break
        removing.append(i)
    return removing


def rstrip(g):
    removing = []
    prev_col = len(lines[0])
    for col_idx in g[::-1]:
        if prev_col - col_idx != 1:
            break
        removing.append(col_idx)
        prev_col -= 1
    return removing


op = input()
if op == "LSTRIP":
    print("\n".join(remove(lines, lstrip(gaps))))
elif op == "RSTRIP":
    print("\n".join(remove(lines, rstrip(gaps))))
elif op == "STRIP":
    print("\n".join(remove(lines, lstrip(gaps) + rstrip(gaps))))
elif op == "STRIP_ALL":
    print("\n".join(remove(lines, gaps)))
else:
    print("Invalid command")
