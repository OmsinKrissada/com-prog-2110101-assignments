pattern, text = input(), input()

sanitized = ''

for c in text:
    ascii_num = ord(c)
    if (ascii_num >= 65 and ascii_num <= 65+25) or (ascii_num >= 97 and ascii_num <= 97+25):
        sanitized += c
    else:
        sanitized += ' '

count = 0
for word in sanitized.split():
    if word == pattern:
        count += 1

print(count)