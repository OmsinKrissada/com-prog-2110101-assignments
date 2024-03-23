full = []
with open(input().strip()) as f:
    for line in f.read().splitlines():
        if line == "":
            continue
        full += line.strip().split("_")

buffer = []
buffer_length = 0
print("-" * 50)
for w in full:
    if buffer_length + len(w) > 50:
        print("_".join(buffer))
        buffer = [w]
        buffer_length = len(w) + 1
    else:
        buffer.append(w)
        buffer_length += len(w) + 1
print("_".join(buffer))
