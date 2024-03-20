raw = input()
transformed = ""
after_space = False
for c in raw:
    if c == " ":
        after_space = True
        continue
    if c.isalnum():
        transformed += c.upper() if after_space else c.lower()
        after_space = False
print(transformed)
