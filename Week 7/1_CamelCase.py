raw = input()
transformed = ""
after_space = False
for c in "".join([x if x.isalnum() else " " for x in raw]).strip():
    if c.isalnum():
        transformed += c.upper() if after_space else c.lower()
        after_space = False
    else:
        after_space = True
print(transformed)
