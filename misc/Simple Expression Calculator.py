exp = input()

num_buffer = ""
num_storage = []
for c in exp:
    if len(num_buffer) == 0:
        num_buffer += c
    elif c >= "0" and c <= "9":
        num_buffer += c
    elif c == "-":
        num_storage.append(int(num_buffer))
        num_buffer = "-"
    else:
        num_storage.append(int(num_buffer))
        num_buffer = ""
num_storage.append(int(num_buffer))
num_buffer = ""
print(sum(num_storage))
