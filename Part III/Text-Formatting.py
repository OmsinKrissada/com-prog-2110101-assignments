filename = input().strip()
# filename = "ignore/text_formatting_data1.txt"
# filename = "ignore/text_formatting_data2.txt"

limit = int(input())
# limit = 26

ruler = ""
for i in range(limit // 10):
    ruler += "-" * 9 + str(i + 1)
if limit % 10 != 0:
    ruler += "-" * (limit % 10)
print(ruler)

with open(filename) as f:
    data = ".".join([l.strip() for l in f.readlines()])

spacing_buffer = ""
word_buffer = ""
wasWord = True
pairs = []
for c in data:
    if c == ".":
        if wasWord:
            pairs.append((word_buffer, spacing_buffer))
            spacing_buffer = word_buffer = ""
            wasWord = False
        spacing_buffer += "."
    else:
        wasWord = True
        word_buffer += c
pairs.append((word_buffer, spacing_buffer))

# print(pairs)

lines = []
line_buffer = ""
for c, s in pairs:
    if len(line_buffer) + len(c) + len(s) > limit:
        lines.append(line_buffer)
        line_buffer = c
    else:
        line_buffer += s + c
lines.append(line_buffer)

print("\n".join(lines))
